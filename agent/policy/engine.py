"""Maps file context and detection findings to ALLOW, WARN, or BLOCK."""


def evaluate_policy(context, detection_result):
    """Return a normalized policy result using common.schemas."""
    raise NotImplementedError
