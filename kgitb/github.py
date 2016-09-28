"""Github API module."""
import logging

import requests

from .config import GH_TOKEN
from .config import HIDDEN
from .config import INFO
from .config import STATUS_CONTEXT

log = logging.getLogger(__name__)


def protect(string):
    return string.replace('[', r'\[')


def quote(string):
    return '>' + string.replace('\n', '\n>')


def get_commits(url):
    commits = requests.get(url, params={'access_token': GH_TOKEN})
    return commits.json()


def get_comments(url):
    comments = requests.get(url, params={'access_token': GH_TOKEN})
    result = []
    for comment in comments.json():
        if comment['body'].startswith(HIDDEN):
            result.append(comment)
    return result


def delete_comment(comment):
    requests.delete(comment['url'], params={'access_token': GH_TOKEN})


def upsert_comment(url, messages):
    comments = get_comments(url)
    message = HIDDEN + '\n\n'.join(messages) + 'More info [here](%s)' % INFO

    if len(messages) == 0:
        for comment in comments:
            delete_comment(comment)
    else:
        if len(comments) > 1:
            for comment in comments:
                delete_comment(comment)
            create_comment(url, message)
        if len(comments) == 1:
            if comments[0]['body'] != message:
                update_comment(comments[0], message)
        else:
            create_comment(url, message)


def update_comment(comments, body):
    requests.patch(comments['url'],
                   params={'access_token': GH_TOKEN},
                   json={'body': body})


def create_comment(url, body):
    requests.post(url,
                  params={'access_token': GH_TOKEN},
                  json={'body': body})


def update_status(url, state, message):
    requests.post(url,
                  params={'access_token': GH_TOKEN},
                  json={'state': state,
                        'context': STATUS_CONTEXT,
                        'description': message})
