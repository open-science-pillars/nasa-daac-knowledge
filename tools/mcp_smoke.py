#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["mcp"]
# ///
"""mcp_smoke: verify the NASA Earthdata MCP server's tool surface.

Connects over Streamable HTTP, initializes a session, lists tools, and
checks the seven documented Earthdata tools are present (get_keywords,
get_collections, get_granules, get_services, get_tools, get_citations,
get_variables), printing each tool's top-level input parameters so the
skills documentation can cite real schemas rather than remembered ones.
With --probe-tool it calls one tool and prints the result, which is the
live no-login proof: a successful get_collections with no credentials
configured is the whole point.

Usage:
  mcp_smoke.py                                   (remote endpoint)
  mcp_smoke.py http://127.0.0.1:5001/mcp/v1      (local dev server)
  mcp_smoke.py --probe-tool get_collections --probe-args '{"keyword": "ECCO"}'

Exit 0 when all seven tools are present; probe failures are reported but
only fail the run with --strict-probe (network to CMR is required for a
probe to succeed).
"""

import argparse
import asyncio
import json
import sys

from mcp import ClientSession

try:  # mcp >= late-2026 API
    from mcp.client.streamable_http import streamable_http_client as _http_client
except ImportError:  # older mcp releases
    from mcp.client.streamable_http import streamablehttp_client as _http_client

EXPECTED = {"get_keywords", "get_collections", "get_granules", "get_services",
            "get_tools", "get_citations", "get_variables"}


async def run(url: str, probe_tool: str | None, probe_args: dict,
              strict_probe: bool) -> int:
    async with _http_client(url) as streams:
        read, write = streams[0], streams[1]
        async with ClientSession(read, write) as session:
            info = await session.initialize()
            server = getattr(info, "server_info", None) or getattr(info, "serverInfo", None)
            print(f"connected: {url}"
                  + (f"  server: {server.name} {server.version}" if server else ""))

            tools = (await session.list_tools()).tools
            names = {t.name for t in tools}
            for t in sorted(tools, key=lambda t: t.name):
                schema = getattr(t, "input_schema", None) or getattr(t, "inputSchema", None) or {}
                params = sorted(schema.get("properties", {}).keys())
                print(f"  {t.name:<16} params: {', '.join(params) if params else '(none)'}")
            missing = sorted(EXPECTED - names)
            extra = sorted(names - EXPECTED)
            if extra:
                print(f"note: undocumented tools present: {', '.join(extra)}")
            if missing:
                print(f"FAIL: expected tools missing: {', '.join(missing)}")
                return 1
            print(f"tool surface OK: all {len(EXPECTED)} documented tools present")

            if probe_tool:
                try:
                    result = await session.call_tool(probe_tool, probe_args)
                    body = "".join(getattr(c, "text", "") for c in result.content)
                    is_err = getattr(result, "is_error", getattr(result, "isError", False))
                    print(f"probe {probe_tool}: "
                          f"{'ERROR' if is_err else 'OK'}\n{body[:600]}")
                    if is_err and strict_probe:
                        return 1
                except Exception as e:
                    print(f"probe {probe_tool}: transport error: {e}")
                    if strict_probe:
                        return 1
            return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("url", nargs="?", default="https://cmr.earthdata.nasa.gov/mcp/v1")
    ap.add_argument("--probe-tool", default=None)
    ap.add_argument("--probe-args", default="{}", help="JSON object of arguments")
    ap.add_argument("--strict-probe", action="store_true")
    ap.add_argument("--debug", action="store_true", help="re-raise instead of the one-line connection message")
    args = ap.parse_args()
    try:
        probe_args = json.loads(args.probe_args)
    except json.JSONDecodeError as e:
        print(f"--probe-args is not valid JSON: {e}", file=sys.stderr)
        return 2
    try:
        return asyncio.run(run(args.url, args.probe_tool, probe_args, args.strict_probe))
    except BaseException as e:  # noqa: BLE001 - connection failures arrive as ExceptionGroups
        if isinstance(e, (KeyboardInterrupt, SystemExit)) or args.debug:
            raise
        print(f"connection failed: {args.url} ({type(e).__name__}); is the server "
              f"reachable from this network?", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
