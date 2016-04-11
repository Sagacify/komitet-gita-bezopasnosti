
def check_for_tabs(commit_message):
    r"""Check for tabs.

    >>> check_for_tabs("This is a good commit.")

    >>> check_for_tabs("This is a\tbad commit.")
    'Use soft tabs!'
    """
    if commit_message.find("\t") != -1:
        return "Use soft tabs!"
