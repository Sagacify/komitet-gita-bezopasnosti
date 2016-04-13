import logging
import sys

from .config import GH_TOKEN
from . import app

log = logging.getLogger(__name__)


def main():
    app.run(host='0.0.0.0')


if __name__ == '__main__':
    if GH_TOKEN is None:
        sys.exit("GH_TOKEN must be set.")
    logging.basicConfig(level=logging.DEBUG)
    main()
