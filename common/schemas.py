"""Shared result and event schemas.

Keep field names and allowed values stable across Agent and Server.
The initial implementation uses plain dictionaries to keep the prototype small.
"""

DECISIONS = {"ALLOW", "WARN", "BLOCK"}
SEVERITIES = {"low", "medium", "high", "critical"}
ENFORCEMENT_STATUSES = {"SUCCESS", "FAILED", "NOT_REQUIRED"}


def make_detection_result(findings):
    """Build a normalized detection result from a list of findings."""
    return {
        "sensitive": bool(findings),
        "findings": findings,
    }


def make_policy_result(decision, reason, policy_id="default"):
    """Build a normalized policy result."""
    decision = decision.upper()
    if decision not in DECISIONS:
        raise ValueError(f"Unsupported decision: {decision}")
    return {
        "decision": decision,
        "reason": reason,
        "policy_id": policy_id,
    }
