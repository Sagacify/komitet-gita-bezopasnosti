from distutils.core import setup
setup(
    name='kgitb',
    packages=['kgitb', 'kgitb.rules'],
    scripts=['bin/resident'],
    version='0.0.4',
    description='A commit message linter',
    author='Augustin Borsu',
    author_email='dev@sagacify.com',
    url='https://github.com/Sagacify/komitet-gita-bezopasnosti',
    extras_require={
        'WEB':  ["flask", "requests"]
    }

)
