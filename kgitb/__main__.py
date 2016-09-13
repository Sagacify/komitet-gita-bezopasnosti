import logging
import sys

from flask import Flask

from .config import GH_TOKEN, HOST, PORT, HIDDEN
from . import routes

LOG = logging.getLogger(__name__)


def main():
    app = routes.setup(Flask(HIDDEN[1:-1]))
    app.run(host=HOST, port=PORT)


if __name__ == '__main__':
    if GH_TOKEN is None:
        sys.exit("GH_TOKEN must be set.")
    LOG.basicConfig(level=logging.DEBUG)
    main()
