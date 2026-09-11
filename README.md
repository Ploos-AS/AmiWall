# AmiWall

AmiWall is a lightweight firewall and network-policy project for classic AmigaOS.

The long-term goal is to provide useful host-side network access control, logging and policy enforcement on classic Amiga systems while remaining practical on real 68k hardware and interoperating with common Amiga TCP/IP stacks.

## Project goals

- Classic AmigaOS first.
- Target AmigaOS 2.04+ where practical.
- Target 68000 and higher CPUs where practical.
- Keep memory and CPU overhead low enough for classic hardware.
- Define a small, human-readable firewall rule language.
- Support explicit allow/deny policy for inbound and outbound traffic where the active TCP/IP stack permits enforcement.
- Log connection and policy decisions in a machine-readable form.
- Design for AmiTCP, Roadshow and Miami compatibility where technically possible.
- Keep policy evaluation independent from stack-specific enforcement adapters.
- Add ARexx control/status integration where useful.
- Integrate cleanly with AmiGuard/AmiForensics-style monitoring without making them dependencies.

## Important M0 limitation

M0 is a design and repository baseline only. AmiWall does **not** yet claim to intercept, block or allow real network traffic. Stack-specific enforcement begins only after capability research and runtime qualification.

## Proposed rule model

Example syntax:

```text
ALLOW OUT TCP ANY 80
ALLOW OUT TCP ANY 443
ALLOW OUT UDP ANY 53
DENY  OUT ANY ANY ANY
ALLOW IN  TCP 192.168.1.0/24 23
DENY  IN  ANY ANY ANY
```

The grammar is intentionally provisional in M0. Rules will be parsed and validated before any enforcement code is added.

## Repository layout

```text
src/                 Native AmiWall source code
include/             Public/internal headers
rules/               Example and default policy files
docs/                Design, stack research and milestone documentation
tools/               Host-side validation/development tools
```

## Milestones

- **M0 — Foundation:** scope, architecture, rule-format draft and qualification gate.
- **M1 — Rule engine:** parse and evaluate rules locally with no packet interception.
- **M2 — Stack capability matrix:** qualify AmiTCP/Roadshow/Miami integration paths and select first enforcement backend.
- **M3 — First enforcement backend:** implement and qualify real filtering for one supported stack.
- **M4 — Logging/status:** structured decision logs, counters and runtime status.
- **M5 — Additional stacks:** add further enforcement adapters where technically viable.
- **M6 — Configuration tooling:** rule validation, reload and safe fallback behaviour.
- **M7 — ARexx/integration:** control/status interface and security-tool integration hooks.
- **M8 — Hardening:** failure modes, resource limits, malformed-input handling and recovery.
- **M9 — Release qualification:** emulator/real-hardware qualification and release packaging.

See [docs/ROADMAP.md](docs/ROADMAP.md).

## M0 qualification

Run:

```sh
python3 tools/check_m0.py
```

Expected result:

```text
M0 PASS
```

## License

MIT. See [LICENSE](LICENSE).

Copyright (c) 2026 Ploos AS.
