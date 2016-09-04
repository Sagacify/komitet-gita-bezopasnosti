import logging
import sys

from .config import GH_TOKEN, HOST, PORT
from . import app

log = logging.getLogger(__name__)


def main():
    app.run(host=HOST, port=PORT)


if __name__ == '__main__':
    if GH_TOKEN is None:
        sys.exit("GH_TOKEN must be set.")
    logging.basicConfig(level=logging.DEBUG)
    main()
