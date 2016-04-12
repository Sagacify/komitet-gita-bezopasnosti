r"""Rule module.

This module and sub-modules contain all the rules that can be applied
to the commit messages.


>>> good_message = '''fix(kgb): Make kgb reliable
...
... We used docstrings to keep the tests as close as possible to the codes.
... Look! That line was exactly 72 characters long!!!
... Yes I know that came at the price of an extra s at code.
... '''

>>> bad_message = '''fixes(k g b): Make it quick and dirty, make it bads
... We try to make explanations as understandable as possible but we have some
... \tissues with code consistency.'''

>>> len(apply(good_message))
0
>>> len(apply(bad_message))
5
"""

import re
from inspect import getmembers, isfunction
from . import line_rules
from . import raw_rules
from . import status_rules


def _get_rules(module):
    """Get all functions from a module."""
    return [tup[1] for tup in getmembers(module, isfunction)
            if tup[0][0] != "_"]

_line_rules = _get_rules(line_rules)
_raw_rules = _get_rules(raw_rules)
_status_rules = _get_rules(status_rules)


def split_lines(commit_message):
    return re.split('\r?\n', commit_message)


def apply(commit_message):
    """Apply all rules to the commit message."""
    errors = []
    for rule in _raw_rules:
        err = rule(commit_message)
        if err is not None:
            errors.append(err)
    commit_lines = split_lines(commit_message)
    for rule in _status_rules:
        err = rule(commit_lines[0])
        if err is not None:
            errors.append(err)
    for check in _line_rules:
        err = check(commit_lines)
        if err is not None:
            errors.append(err)
    return(errors)
