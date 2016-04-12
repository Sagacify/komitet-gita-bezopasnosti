from .. import MAX_STATUS_LENGTH
from .. import STATUS_R

def _is_merge(status_line):
    return status_line.startswith("Merge pull request #")


def check_status_length(status_line):
    """Check status length.

    >>> check_status_length("this is short enough")

    >>> check_status_length("TOO_LONG" * 10)
    'Limit status to 50 characters'
    """
    if not _is_merge(status_line):
        if len(status_line) > MAX_STATUS_LENGTH:
            return "Limit status to {0} characters".format(MAX_STATUS_LENGTH)


def check_status_formatting(status_line):
    """Check status formatting.
    >>> check_status_formatting("fix(this): This is good")

    >>> check_status_formatting("fix(th)is): This is not good")
    'Conform status to `<type>(<scope>): <subject>` pattern'

    >>> check_status_formatting("fix(th is): This is not good")
    'Conform status to `<type>(<scope>): <subject>` pattern'
    """
    errors = []
    if not _is_merge(status_line):
        if STATUS_R.match(status_line) is None:
            errors.append(
                "Conform status to `<type>(<scope>): <subject>` pattern")
            return "\n".join(errors)
