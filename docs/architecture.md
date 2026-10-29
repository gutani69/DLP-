# Architecture

## Components

- **Agent:** observes supported file events and coordinates the DLP pipeline.
- **Detection:** inspects supported file content and returns normalized findings.
- **Policy:** maps context and findings to `ALLOW`, `WARN`, or `BLOCK`.
- **Enforcement:** applies a decision through a specific tested control.
- **Server:** Flask API, local event persistence, and dashboard delivery.
- **Common:** shared schemas and stable decision/status values.

## Communication

Detection, policy, and enforcement are Python modules called by the agent. The agent sends event records to the server over HTTP using JSON. The dashboard calls the server API; it does not call agent internals directly.

## Shared event contract

An event should include an event ID, agent ID, file name, file hash, detection findings, policy decision, and enforcement status. Do not include raw sensitive values or file contents in logs.

Allowed decisions: `ALLOW`, `WARN`, `BLOCK`.
Allowed enforcement statuses: `SUCCESS`, `FAILED`, `NOT_REQUIRED`.

## Current limitations

The scaffold does not yet provide full monitoring, content inspection, event persistence, or upload blocking. A file watcher alone does not stop uploads through arbitrary applications. Enforcement must be tied to a supported transfer path or OS control and tested independently.
