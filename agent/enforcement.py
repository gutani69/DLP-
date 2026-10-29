"""Enforcement adapter boundary.

A returned BLOCK decision is not enforcement by itself. Implement and test a
specific supported transfer path or OS control before reporting success.
"""


def enforce_decision(path, decision):
    """Apply an enforcement decision and return an explicit outcome."""
    raise NotImplementedError
