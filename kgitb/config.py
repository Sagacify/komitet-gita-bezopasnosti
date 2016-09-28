# -*- coding: utf-8 -*-
from os import environ as env

# Identifier used to recognize auto-generated comments
HIDDEN = '<KGB>'
STATUS_CONTEXT = 'Комитет Git\'a Безопасности'

MAX_STATUS_LENGTH = int(env.get('MAX_STATUS_LENGTH') or 50)
MAX_LINE_LENGTH = int(env.get('MAX_LINE_LENGTH') or 72)

_DEFAULT_TYPES = ','.join([
    'chore',
    'doc',
    'feat',
    'fix',
    'perf',
    'refactor',
    'revert',
    'style',
    'test',
    'version'])
TYPES = frozenset((env.get('AUTHORIZED_TYPES') or _DEFAULT_TYPES).split(','))

GH_TOKEN = env.get('GH_TOKEN')

HOST = env.get('KGB_HOST') or '0.0.0.0'
PORT = env.get('KGB_PORT') or 5000

INFO = 'https://github.com/sagacify/komitet-gita-bezopasnosti'
