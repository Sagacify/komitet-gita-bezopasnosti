from ..config import MAX_LINE_LENGTH


def check_second_line(commit_lines):
    r"""Check second line is blank line and there is a body.

    >>> from . import split_lines
    >>> check_second_line(split_lines('first line\n\nbody'))

    >>> check_second_line(split_lines('first line\nbody'))
    'Separate status and body with an empty line.'
    """
    if len(commit_lines) > 1 and len(commit_lines[1]) > 0:
        return 'Separate status and body with an empty line.'


def check_body_line_length(commit_lines):
    """Check line length.

    >>> check_body_line_length(["", "", 'this is short enough'])

    >>> check_body_line_length(["", "", 'TOO_LONG' * 10])
    'Wrap body lines at 72 characters'
    """
    for line in commit_lines:
        if len(line) > MAX_LINE_LENGTH:
            return 'Wrap body lines at {0} characters'.format(MAX_LINE_LENGTH)


def check_for_tabs(commit_lines):
    r"""Check for tabs.

    >>> check_for_tabs(['This is a good commit.'])

    >>> check_for_tabs(['This is a\tbad commit.'])
    'Use soft tabs!'
    """
    for line in commit_lines:
        if line.find('\t') != -1:
            return 'Use soft tabs!'
