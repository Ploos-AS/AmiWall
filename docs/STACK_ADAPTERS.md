# AmiWall stack adapter architecture

AmiWall must not assume that every Amiga TCP/IP stack exposes the same filtering hooks.

The core therefore owns policy semantics while adapters own integration with a specific stack.

## Core responsibilities

- parse and validate rules
- normalize policy
- evaluate synthetic/runtime connection metadata
- maintain counters
- emit structured decisions
- expose configuration/status

## Adapter responsibilities

- detect whether a supported stack is available
- report adapter capabilities precisely
- translate stack events/operations into AmiWall's neutral model
- enforce ALLOW/DENY only where the stack provides a technically sound mechanism
- report when a requested policy cannot be enforced

## Initial research targets

- AmiTCP and compatible `bsdsocket.library` environments
- Roadshow
- Miami / MiamiDX

M2 will produce a capability matrix before the first enforcement adapter is selected.

## Capability language

Adapters should eventually identify capabilities such as:

- `observe_outbound`
- `observe_inbound`
- `block_outbound`
- `block_inbound`
- `tcp`
- `udp`
- `address_match`
- `port_match`

A capability must not be advertised until demonstrated or supported by documented stack interfaces.
