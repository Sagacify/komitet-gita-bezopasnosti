from distutils.core import setup
import io
import os


readme = 'README.md'
if os.path.isfile('./README.rst'):
    readme = 'README.rst'

print('Using %s as readme' % readme)
with io.open(readme, encoding='utf-8') as file:
    readme = file.read()

setup(
    name='kgitb',
    packages=['kgitb', 'kgitb.rules'],
    scripts=['bin/resident'],
    version='0.1.4',
    description='A commit message linter',
    long_description=readme,
    author='Augustin Borsu',
    author_email='dev@sagacify.com',
    url='https://github.com/Sagacify/komitet-gita-bezopasnosti',
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
