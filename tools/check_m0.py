#!/usr/bin/env python3
"""AmiWall M0 repository qualification gate."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "LICENSE",
    "docs/ROADMAP.md",
    "docs/RULE_FORMAT.md",
    "docs/STACK_ADAPTERS.md",
    "rules/example.rules",
    "src/README.md",
    "include/README.md",
    "tools/check_m0.py",
]

RULE_RE = re.compile(
    r"^(ALLOW|DENY)\s+(IN|OUT)\s+(TCP|UDP|ANY)\s+"
    r"(ANY|(?:\d{1,3}\.){3}\d{1,3}(?:/\d{1,2})?)\s+"
    r"(ANY|\d{1,5})$"
)


def fail(message: str) -> None:
    print(f"M0 FAIL: {message}")
    raise SystemExit(1)


def validate_rules(path: Path) -> None:
    active = 0
    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        active += 1
        match = RULE_RE.fullmatch(line)
        if not match:
            fail(f"{path}:{lineno}: invalid example rule: {line}")
        peer = match.group(4)
        port = match.group(5)
        if peer != "ANY":
            address, _, prefix = peer.partition("/")
            octets = address.split(".")
            if any(int(octet) > 255 for octet in octets):
                fail(f"{path}:{lineno}: invalid IPv4 address")
            if prefix and int(prefix) > 32:
                fail(f"{path}:{lineno}: invalid IPv4 prefix")
        if port != "ANY" and int(port) > 65535:
            fail(f"{path}:{lineno}: invalid port")
    if active == 0:
        fail("example policy has no active rules")


def main() -> int:
    missing = [name for name in REQUIRED if not (ROOT / name).is_file()]
    if missing:
        fail("missing required files: " + ", ".join(missing))

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for marker in ("AmigaOS 2.04+", "68000", "AmiTCP", "Roadshow", "Miami", "does **not** yet claim"):
        if marker not in readme:
            fail(f"README missing marker: {marker}")

    adapters = (ROOT / "docs/STACK_ADAPTERS.md").read_text(encoding="utf-8")
    for marker in ("policy", "adapter", "AmiTCP", "Roadshow", "Miami"):
        if marker.lower() not in adapters.lower():
            fail(f"stack adapter document missing marker: {marker}")

    validate_rules(ROOT / "rules/example.rules")

    print("M0 PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
