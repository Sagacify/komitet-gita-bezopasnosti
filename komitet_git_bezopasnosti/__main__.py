import logging
import sys

from flask import Flask
import flask

from . import GH_TOKEN
from . import HIDDEN
from . import github
from. import rules

log = logging.getLogger(name=HIDDEN[1:-1])


def check_pr(commits_url, comments_url, status_url):
    # status = True
    github.update_status(status_url)
    all_errors = 0
    messages = []
    for commit in github.get_commits(commits_url):
        message = commit["commit"]["message"]
        errors = rules.apply(message)
        if len(errors) > 0:
            sha = commit["sha"]
            messages.append("\n".join([sha, github.quote(message), ""] +
                                      errors))
            all_errors += len(errors)

    log.debug(all_errors)
    github.upsert_comment(comments_url, messages)
    github.update_status(status_url, errors)


def github_pr():
    body = flask.request.json
    if body is None:
        return "", 500
    keys = body.keys()
    if "action" not in keys or "pull_request" not in keys:
        log.error({"error": "not_a_pull_request", "body": body})
        return "", 500
    elif body["action"] in {"assigned", "unassigned",
                            "labeled", "unlabeled", "closed"}:
        log.debug({"event": "non_event", "body": body})
        return "", 200
    elif body["action"] in {"opened", "reopened", "synchronize"}:
        log.debug({"event": "analyse_pr", "body": body})
        check_pr(body["pull_request"]["commits_url"],
                 body["pull_request"]["comments_url"],
                 body["pull_request"]["statuses_url"])
        return ""

    return "", 204


def main():
    app = Flask(__name__)

    app.add_url_rule('/github/pr',
                     'github_pr',
                     github_pr,
                     methods=["POST"])
    app.run(host='0.0.0.0')


if __name__ == '__main__':
    if GH_TOKEN is None:
        sys.exit("GH_TOKEN must be set.")
    logging.basicConfig(level=logging.DEBUG)
    main()
