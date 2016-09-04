from flask import Flask

from . import routes
from . import config

app = routes.setup(Flask(config.HIDDEN[1:-1]))
