# DLP — Data Loss Prevention

A graduation-project scaffold for a prototype **Data Loss Prevention (DLP)** platform, with planned endpoint monitoring and automated security-configuration checks.

## Repository layout

- `common/` — shared schemas and data structures
- `agent/` — endpoint-side monitoring and enforcement adapters
- `detection/` — sensitive-data detection engine
- `policy/` — allow/warn/block policy decisions
- `server/` — Flask management API
- `dashboard/` — future administrator UI
- `tests/` — automated tests
- `docs/` — architecture and design notes
- `deploy/` — container/deployment assets

## Quick start

Requires Python 3.11 or newer.

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
python -m pip install -e ".[dev]"
pytest
python -m server.app
```

Then open `http://127.0.0.1:5000/health` or `/api/v1/status`.

## Current status

This repository is an initial scaffold, not a production DLP product. Detection currently uses simple text-marker matching. Policy decisions are prototypes; no app-independent upload blocking, operating-system enforcement, authentication, persistent audit storage, or configuration remediation is implemented yet.

## Planned work

1. Expand file inspection and define sensitive-data rules.
2. Add policy configuration and audit events.
3. Design and implement endpoint enforcement with a documented threat model.
4. Add configuration-compliance checks and safe remediation.
5. Build the admin dashboard, authentication, and persistence.
6. Add integration tests and deployment hardening.

## Security notes

- Never commit credentials, tokens, real sensitive documents, or local `.env` files.
- Avoid recording file contents in logs.
- Treat any enforcement result as advisory until an OS-level or network enforcement control is implemented and tested.
