# AmiWall Roadmap

## Architecture principle

AmiWall separates policy from enforcement:

1. **Rule parser / evaluator** — stack-independent policy representation and matching.
2. **Runtime core** — configuration, counters, logging and safe reload behaviour.
3. **Stack adapters** — implementation-specific hooks for supported Amiga TCP/IP stacks.

This separation lets rule parsing and policy semantics be tested before AmiWall gains any capability to affect real network traffic.

## M0 — Foundation

Acceptance criteria:

- Scope and non-goals documented.
- MIT license present.
- Source/include/rules/docs/tools layout established.
- Draft rule syntax documented.
- Example baseline policy present.
- Stack adapter architecture documented.
- Host-side `tools/check_m0.py` validates the baseline.
- Documentation explicitly states that M0 performs no real filtering.

## M1 — Rule engine

Implement a small native rule parser and evaluator with deterministic first-match semantics. No network interception.

Planned capabilities:

- ALLOW / DENY
- IN / OUT
- TCP / UDP / ANY
- source/address match
- destination port match
- ANY wildcard
- syntax validation
- explicit default policy

M1 qualification will use synthetic connection tuples only.

## M2 — Stack capability matrix

Research and qualify integration points for:

- AmiTCP / compatible bsdsocket.library environments
- Roadshow
- Miami / MiamiDX

Document what can actually be enforced, observed or merely approximated on each stack. Select the first viable backend based on technical evidence rather than preference.

## M3 — First enforcement backend

Implement real filtering for the selected stack. Qualification must demonstrate known ALLOW/DENY cases under an emulator or real Amiga environment.

Fail-open/fail-closed behaviour must be explicit and documented.

## M4 — Logging and status

Add structured decision logs, rule hit counters, active policy status and diagnostics suitable for local inspection and external collection.

## M5 — Additional stack adapters

Add other viable TCP/IP stacks without changing rule semantics unnecessarily.

## M6 — Configuration tooling

Add policy validation, atomic/safe reload where practical, dry-run and recovery from invalid configuration.

## M7 — ARexx and integration

Add an ARexx interface where practical for status, reload and diagnostics. Provide optional integration hooks for other Ploos-AS Amiga security tooling.

## M8 — Hardening

Exercise malformed rules, resource exhaustion, large rule sets, logging failures, stack loss/restart and recovery behaviour.

## M9 — Release qualification

Qualify supported OS/CPU/stack combinations, produce release archives and document known limitations clearly.
