"""Github API module."""
import logging

import requests

from .config import HIDDEN
from .config import GH_TOKEN
from .config import STATUS_CONTEXT

log = logging.getLogger(__name__)


def protect(string):
    return string.replace("[", "\[")


def quote(string):
    return ">" + string.replace("\n", "\n>")


def get_commits(url):
    commits = requests.get(url, params={"access_token": GH_TOKEN})
    return commits.json()


def get_comments(url):
    comments = requests.get(url, params={"access_token": GH_TOKEN})
    result = []
    for comment in comments.json():
        if comment["body"].startswith(HIDDEN):
            result.append(comment)
    return result


def delete_comment(comment):
    requests.delete(comment["url"], params={"access_token": GH_TOKEN})


def upsert_comment(url, messages):
    comments = get_comments(url)
    message = HIDDEN + "\n\n".join(messages)
    if len(comments) > 1:
        log.error({"error": "not_supposed_to_happen",
                   "comments": comments})
        for comment in comments:
            delete_comment(comment)
    elif len(comments) == 1:
        if comments[0]["body"] != message:
            update_comment(comments[0], message)
    else:
        create_comment(url, message)


def update_comment(comments, body):
    requests.patch(comments["url"],
                   params={"access_token": GH_TOKEN},
                   json={"body": body})


def create_comment(url, body):
    requests.post(url,
                  params={"access_token": GH_TOKEN},
                  json={"body": body})


def update_status(url, errors=None):
    if errors is None:
        requests.post(url,
                      params={"access_token": GH_TOKEN},
                      json={"state": "pending",
                            "context": STATUS_CONTEXT,
                            "description": "KGB is reviewing your commits."})
    elif errors == 0:
        requests.post(url,
                      params={"access_token": GH_TOKEN},
                      json={"state": "success",
                            "context": STATUS_CONTEXT,
                            "description": "We are proud of you!"})
    else:
        requests.post(url,
                      params={"access_token": GH_TOKEN},
                      json={"state": "error",
                            "context": STATUS_CONTEXT,
                            "description":
                            "Fix the {} errors found!".format(errors)})
