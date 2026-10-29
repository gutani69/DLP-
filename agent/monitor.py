"""Endpoint file-event monitoring boundary.

TODO: implement a platform-specific monitor and document which events it observes.
A file watcher alone cannot reliably identify or block every upload.
"""


def collect_file_context(path):
    """Return normalized metadata for a candidate file."""
    raise NotImplementedError
