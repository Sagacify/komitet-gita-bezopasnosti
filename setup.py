from distutils.core import setup
import io
import os

from kgitb.__about__ import (
    __title__, __summary__, __uri__, __version__,
    __author__, __email__
)


readme = 'README.md'
if os.path.isfile('./README.rst'):
    readme = 'README.rst'

print('Using %s as readme' % readme)
with io.open(readme, encoding='utf-8') as file:
    readme = file.read()

setup(
    name=__title__,
    packages=['kgitb', 'kgitb.rules'],
    scripts=['bin/resident'],
    version=__version__,
    description=__summary__,
    long_description=readme,
    author=__author__,
    author_email=__email__,
    url=__uri__,
    extras_require={
        'WEB': ['flask', 'requests']
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: ' +
        'GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Topic :: Text Processing'
    ],
    keywords='git lint russian_history'
)
