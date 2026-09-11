# AmiWall rule format — draft v0

M0 defines a deliberately small, human-readable rule language. It is not frozen and does not imply that real packet filtering is implemented.

## Syntax

```text
ACTION DIRECTION PROTOCOL PEER PORT
```

Fields:

- `ACTION`: `ALLOW` or `DENY`
- `DIRECTION`: `IN` or `OUT`
- `PROTOCOL`: `TCP`, `UDP` or `ANY`
- `PEER`: `ANY`, an IPv4 address, or an IPv4 CIDR prefix
- `PORT`: decimal port number or `ANY`

Examples:

```text
ALLOW OUT TCP ANY 80
ALLOW OUT TCP ANY 443
ALLOW OUT UDP ANY 53
DENY  OUT ANY ANY ANY
ALLOW IN TCP 192.168.1.0/24 23
DENY  IN ANY ANY ANY
```

Blank lines and lines beginning with `#` are comments.

## Intended semantics

The intended M1 model is deterministic first-match evaluation from top to bottom. A connection tuple is matched against direction, protocol, peer address and peer port. If no rule matches, an explicit default policy is applied.

M0 does not yet freeze whether IN/OUT `PEER` and `PORT` refer to remote endpoint only or whether later syntax will expose local and remote endpoints separately. M1 must settle this before the grammar is considered executable policy.

## Safety requirements

- Invalid syntax must never be silently accepted.
- Unsupported fields must produce an error rather than being ignored.
- Policy load failure must not accidentally turn an intended deny policy into an allow policy.
- Stack-specific limitations must be visible to the user.
- Logging must distinguish observed traffic from traffic that was actually enforceable.
