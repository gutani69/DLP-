"""Small local event-storage boundary.

TODO: implement SQLite schema, safe serialization, and persistence.
"""


def save_event(event):
    raise NotImplementedError


def list_events(limit=100):
    raise NotImplementedError
