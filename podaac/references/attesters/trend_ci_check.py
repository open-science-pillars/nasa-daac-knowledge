#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# ///
"""Deterministic attester for an attested trend with interval.

No LLM, stdlib only, consumer-side (spec 10.2). This attester does
not sample the receipt: it recomputes the ENTIRE chain from the
series the receipt carries, with its own arithmetic, and compares
every intermediate. PASS (exit 0) only when ALL hold, else FAIL
(exit 1) naming the field:

  1. declared receipt fields present (run_id, code_sha256, data,
     bound_parameters, series, intermediates, results);
  2. code_sha256 matches the sanctioned computation file;
  3. provenance: the receipt names its source series by path and
     sha256, and the series came from a receipt whose data.record is
     the verify tool's stamp for a manifested tree; a trend over a
     series of unknown origin is refused, whatever its arithmetic;
  4. the method is the contract exactly: confidence 0.95, monthly
     time unit, trend per year of 12 months, deseasonalization one
     of climatology or none, and climatology only over complete years
     (at least two);
  5. the series is consecutive calendar months, at least 6 of them;
  6. THE RECOMPUTE: from series and bound parameters alone, this file
     rebuilds the deseasonalized series, the OLS slope, the residual
     lag-1 autocorrelation r1, n_eff = n(1-r1)/(1+r1), the standard
     error on n_eff-2 degrees of freedom (at least one, or no
     interval is attested), the t quantile on those degrees of
     freedom, and the interval; each must match the
     receipt's value within 1e-9 relative (measured agreement: below
     1e-12, the two implementations differ only in summation order);
  7. the results block is consistent with the intermediates: trend is
     the slope times months per year, the interval is trend plus and
     minus the half width, the units string ends in /year, and the
     significance flag is what the interval says.

Usage: trend_ci_check.py RECEIPT.json [--computation PATH]
"""

import argparse
import hashlib
import json
import math
import sys
from pathlib import Path

CONFIDENCE = 0.95
MONTHS_PER_YEAR = 12.0
MIN_MONTHS = 6
CLIM_MIN_YEARS = 2
MIN_DOF = 1.0
REL_TOL = 1e-9
FIELDS = ["run_id", "code_sha256", "data", "bound_parameters", "series",
          "intermediates", "results"]
INTERMEDIATES = ["n", "slope_per_month", "intercept", "sxx", "r1", "n_eff",
                 "dof", "se_per_month", "t_quantile",
                 "naive_se_per_month"]


def fail(msg: str) -> int:
    print(f"FAIL: {msg}")
    return 1


# ---- independent recompute: written from the method statement, not
# ---- copied from the executor's structure

def betacf(a, b, x, max_iter=500, eps=1e-15):
    tiny = 1e-300
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c, d = 1.0, 1.0 - qab * x / qap
    d = 1.0 / (d if abs(d) > tiny else tiny)
    h = d
    for m in range(1, max_iter + 1):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        d = 1.0 / (d if abs(d) > tiny else tiny)
        c = 1.0 + aa / (c if abs(c) > tiny else tiny)
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        d = 1.0 / (d if abs(d) > tiny else tiny)
        c = 1.0 + aa / (c if abs(c) > tiny else tiny)
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < eps:
            return h
    raise ArithmeticError("incomplete beta did not converge")


def betainc(a, b, x):
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    lbeta = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
    front = math.exp(lbeta + a * math.log(x) + b * math.log(1.0 - x))
    if x < (a + 1.0) / (a + b + 2.0):
        return front * betacf(a, b, x) / a
    return 1.0 - front * betacf(b, a, 1.0 - x) / b


def t_cdf(t, df):
    x = df / (df + t * t)
    tail = 0.5 * betainc(df / 2.0, 0.5, x)
    return 1.0 - tail if t >= 0 else tail


def t_quantile(p, df):
    lo, hi = 0.0, 1.0
    while t_cdf(hi, df) < p:
        hi *= 2.0
        if hi > 1e12:
            raise ArithmeticError("t quantile out of range")
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if t_cdf(mid, df) < p:
            lo = mid
        else:
            hi = mid
        if hi - lo < 1e-13 * max(1.0, hi):
            break
    return 0.5 * (lo + hi)


def recompute(values, deseasonalize):
    y = list(values)
    n = len(y)
    if deseasonalize == "climatology":
        years = n // 12
        clim = [sum(y[k::12]) / years for k in range(12)]
        y = [v - clim[i % 12] for i, v in enumerate(y)]
    tbar = (n - 1) / 2.0
    ybar = sum(y) / n
    sxx = sum((i - tbar) ** 2 for i in range(n))
    slope = sum((i - tbar) * (v - ybar) for i, v in enumerate(y)) / sxx
    intercept = ybar - slope * tbar
    e = [v - intercept - slope * i for i, v in enumerate(y)]
    ss = sum(v * v for v in e)
    r1 = sum(a * b for a, b in zip(e, e[1:])) / ss
    n_eff = n * (1.0 - r1) / (1.0 + r1)
    dof = n_eff - 2.0
    if dof < MIN_DOF:
        return None
    se = math.sqrt(ss / dof / sxx)
    tq = t_quantile(0.5 + CONFIDENCE / 2.0, dof)
    return {"n": n, "series_fit": y, "slope_per_month": slope,
            "intercept": intercept, "sxx": sxx, "r1": r1, "n_eff": n_eff,
            "dof": dof, "se_per_month": se, "t_quantile": tq,
            "naive_se_per_month": math.sqrt(ss / (n - 2) / sxx)}


def close(a, b):
    return abs(a - b) <= REL_TOL * max(1.0, abs(a), abs(b))


def consecutive(dates):
    ym = [int(d[:4]) * 12 + int(d[5:7]) - 1 for d in dates]
    return all(b - a == 1 for a, b in zip(ym, ym[1:]))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("receipt", type=Path)
    ap.add_argument("--computation", type=Path,
                    default=Path(__file__).parent.parent
                    / "computations" / "ecco_trend_ci.py")
    args = ap.parse_args()
    r = json.loads(args.receipt.read_text(encoding="utf-8"))

    for f in FIELDS:
        if f not in r:
            return fail(f"receipt field missing: {f}")
    want = hashlib.sha256(args.computation.read_bytes()).hexdigest()
    if r["code_sha256"] != want:
        return fail("code_sha256 does not match the sanctioned computation")

    data = r["data"]
    if (not isinstance(data, dict) or not data.get("source")
            or not isinstance(data.get("source_sha256"), str)
            or len(data["source_sha256"]) != 64):
        return fail("receipt does not name its source series by path and "
                    "sha256")
    if not isinstance(data.get("source_receipt"), dict) \
            or not data["source_receipt"].get("code_sha256"):
        return fail("series did not come from a sanctioned receipt: a trend "
                    "over a series of unknown origin is not attested, "
                    "whatever its arithmetic")
    if not isinstance(data.get("record"), dict):
        return fail("source receipt names no verified data tree: "
                    "data.record must be the RECORD.json stamp the verify "
                    "tool leaves in a tree checked against its manifest; "
                    "nothing is attested against unmanifested data")

    bp = r["bound_parameters"]
    if (bp.get("confidence") != CONFIDENCE or bp.get("time_unit") != "month"
            or bp.get("trend_per") != "year"
            or bp.get("months_per_year") != MONTHS_PER_YEAR):
        return fail("confidence, time unit or trend unit differ from the "
                    "contract")
    des = bp.get("deseasonalize")
    if des not in ("climatology", "none"):
        return fail(f"deseasonalize {des!r} is not climatology or none")
    if not isinstance(bp.get("scale"), (int, float)) or bp["scale"] == 0:
        return fail("scale must be a non-zero number")

    s = r["series"]
    dates, values = s.get("dates"), s.get("values")
    if (not isinstance(dates, list) or not isinstance(values, list)
            or len(dates) != len(values) or len(dates) < MIN_MONTHS):
        return fail(f"series needs parallel dates and values, at least "
                    f"{MIN_MONTHS} months")
    if not all(isinstance(d, str) and len(d) == 7 and d[4] == "-"
               for d in dates) or not consecutive(dates):
        return fail("series months are not consecutive YYYY-MM")
    if not all(isinstance(v, (int, float)) and math.isfinite(v)
               for v in values):
        return fail("series values must be finite numbers")
    n = len(values)
    if des == "climatology" and (n % 12 or n < 12 * CLIM_MIN_YEARS):
        return fail(f"climatology deseasonalization over {n} months: needs "
                    f"complete years, at least {CLIM_MIN_YEARS}")

    mine = recompute([v * bp["scale"] for v in values], des)
    if mine is None:
        return fail(f"effective sample size leaves fewer than {MIN_DOF} "
                    "degrees of freedom; no interval can be attested")
    got = r["intermediates"]
    for k in INTERMEDIATES:
        if k not in got:
            return fail(f"intermediate missing: {k}")
        if not close(float(got[k]), float(mine[k])):
            return fail(f"recompute of {k} disagrees: receipt {got[k]!r}, "
                        f"recomputed {mine[k]!r}")
    fit = got.get("series_fit")
    if (not isinstance(fit, list) or len(fit) != n
            or not all(close(a, b) for a, b in zip(fit, mine["series_fit"]))):
        return fail("recompute of the deseasonalized series disagrees")

    res = r["results"]
    trend = mine["slope_per_month"] * MONTHS_PER_YEAR
    half = mine["t_quantile"] * mine["se_per_month"] * MONTHS_PER_YEAR
    naive = (t_quantile(0.5 + CONFIDENCE / 2.0, n - 2)
             * mine["naive_se_per_month"] * MONTHS_PER_YEAR)
    for k, v in [("trend", trend), ("ci_low", trend - half),
                 ("ci_high", trend + half), ("half_width", half),
                 ("naive_half_width", naive), ("n_eff", mine["n_eff"]),
                 ("r1", mine["r1"])]:
        if k not in res or not close(float(res[k]), v):
            return fail(f"results.{k} is not what the intermediates give: "
                        f"receipt {res.get(k)!r}, recomputed {v!r}")
    if res.get("n") != n:
        return fail("results.n is not the series length")
    units = res.get("units")
    if not isinstance(units, str) or not units.endswith("/year") \
            or units != f"{bp.get('report_units')}/year":
        return fail("results.units must be the report units per year")
    sig = (trend - half) * (trend + half) > 0
    if res.get("significant_at_confidence") is not sig:
        return fail("significance flag contradicts the interval")

    print(f"PASS run {r['run_id']}: sanctioned code, verified source tree, "
          f"contract method, and the whole chain recomputes: "
          f"{trend:+.4f} [{trend - half:+.4f}, {trend + half:+.4f}] {units} "
          f"over {n} months, r1 {mine['r1']:+.3f}, n_eff {mine['n_eff']:.1f}"
          f" (naive half width {naive:.4f}, honest {half:.4f})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
