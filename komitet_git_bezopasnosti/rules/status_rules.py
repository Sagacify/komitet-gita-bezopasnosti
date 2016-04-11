from .. import MAX_STATUS_LENGTH
from .. import STATUS_R


def check_status_length(status_line):
    """Check status length.

    >>> check_status_length("this is short enough")

    >>> check_status_length("TOO_LONG" * 10)
    'Limit status to 50 characters'
    """
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
    if STATUS_R.match(status_line) is None:
        return "Conform status to `<type>(<scope>): <subject>` pattern"
