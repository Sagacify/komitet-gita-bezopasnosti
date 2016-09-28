r"""Rule module.

This module and sub-modules contain all the rules that can be applied
to the commit messages.


>>> good_message = '''fix(kgb): Make kgb reliable
...
... We used docstrings to keep the tests as close as possible to the codes.
... Look! That line was exactly 72 characters long!!!
... Yes I know that came at the price of an extra s at code.
... # This\tline should be ignored as it is a comment. So any violation should
... '''

>>> bad_message = '''fixes(k g b): Make it quick and dirty, make it bads
... We try to make explanations as understandable as possible but we have some
... \tissues with code consistency.'''

>>> len(apply_rules(good_message))
0
>>> len(apply_rules(bad_message))
5
"""

import re
from inspect import getmembers, isfunction
from . import line_rules
from . import status_rules


def get_rules(module):
    """Get all functions from a module."""
    return [tup[1] for tup in getmembers(module, isfunction)
            if tup[0][0] != '_']


line_rules = get_rules(line_rules)
status_rules = get_rules(status_rules)


def is_merge(commit_message):
    return commit_message.startswith('Merge pull request #')


def split_lines(commit_message):
    return re.split('\r?\n', commit_message)


def apply_rules(commit_message):
    """Apply all rules to the commit message."""
    errors = []
    if is_merge(commit_message):
        return errors
    commit_lines = split_lines(commit_message)
    status = commit_lines[0]
    commit_lines = [l for l in commit_lines if not l.startswith('#')]
    for rule in status_rules:
        err = rule(status)
        if err is not None:
            errors.append(err)
    for check in line_rules:
        err = check(commit_lines)
        if err is not None:
            errors.append(err)
    return errors
