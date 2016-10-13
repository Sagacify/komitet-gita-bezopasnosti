import re

from ..config import MAX_STATUS_LENGTH
from ..config import TYPES

STATUS_PATTERN = re.compile(
    r'^([^()\s]*)(\s*)\(([^()\s]*)\)(\s*):(\s*)(.*\S)(\s*)$')

PRETTY_TYPES = ', '.join(sorted(TYPES))


def check_status_length(status_line):
    """Check status length.

    >>> check_status_length('this is short enough')

    >>> check_status_length('TOO_LONG' * 10)
    'Shorten status from {0} to {1} characters'
    """.format(len('TOO_LONG' * 10), MAX_STATUS_LENGTH)
    if len(status_line) > MAX_STATUS_LENGTH:
        return 'Shorten status from {0} to {1} characters'.format(
            len(status_line), MAX_STATUS_LENGTH)


def check_status_formatting(status_line):
    r"""Check status formatting.
    >>> check_status_formatting('fix(this): This is good')

    >>> print(check_status_formatting('fixing(this): This is not good'))
    Begin status with one of the following types:
    *chore, doc, feat, fix, perf, refactor, revert, style, test, version*

    >>> print(check_status_formatting('testing(this): This is not good'))
    Begin status with one of the following types:
    *chore, doc, feat, fix, perf, refactor, revert, style, test, version*

    >>> print(check_status_formatting('fix(th)is): This is not good'))
    Conform status to `<type>(<scope>): <subject>` pattern
    type and scope cannot contain spaces or parenthesis

    >>> print(check_status_formatting('fix(th is): This is not good'))
    Conform status to `<type>(<scope>): <subject>` pattern
    type and scope cannot contain spaces or parenthesis

    >>> print(check_status_formatting('fix (this) :   This is not good'))
    Remove space between type and scope.
    Remove space between scope and colon.
    Use a single space between colon and subject.

    >>> print(check_status_formatting('fix(this):n  '))
    Add space after colon.
    Make subject at least three character long.
    Strip trailing whitespaces from status line.

    >>> check_status_formatting('fix(this): Allow final non-word character.')

    """
    match = STATUS_PATTERN.match(status_line)
    if match is None:
        return ('Conform status to `<type>(<scope>): <subject>` pattern\n' +
                'type and scope cannot contain spaces or parenthesis')
    errors = []
    if match.group(1) not in TYPES:
        errors.append('Begin status with one of the following types:\n' +
                      '*%s*' % PRETTY_TYPES)
    if len(match.group(2)) > 0:
        errors.append('Remove space between type and scope.')
    if len(match.group(4)) > 0:
        errors.append('Remove space between scope and colon.')
    if match.group(5) == '':
        errors.append('Add space after colon.')
    elif match.group(5) != ' ':
        errors.append('Use a single space between colon and subject.')
    if len(match.group(6).strip()) < 3:
        errors.append('Make subject at least three character long.')
    if len(match.group(7)) > 0:
        errors.append('Strip trailing whitespaces from status line.')
    if len(errors) == 0:
        return None
    else:
        return '\n'.join(errors)
