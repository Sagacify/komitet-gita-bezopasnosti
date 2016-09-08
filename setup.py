from distutils.core import setup
import io

try:
    from pypandoc import convert

    def read_md(file):
        convert(file, 'rst')

except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")

    def read_md(file):
        io.open(file, 'r', encoding="utf-8").read()


setup(
    name='kgitb',
    packages=['kgitb', 'kgitb.rules'],
    scripts=['bin/resident'],
    version='0.0.5',
    description='A commit message linter',
    long_description=read_md('README.md'),
    author='Augustin Borsu',
    author_email='dev@sagacify.com',
    url='https://github.com/Sagacify/komitet-gita-bezopasnosti',
    extras_require={
        'WEB':  ["flask", "requests"]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Topic :: Text Processing'
    ],
    keywords='git lint russian_history'
)
