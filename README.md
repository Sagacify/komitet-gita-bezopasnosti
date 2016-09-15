Комитет Git'a Безопасности
==========================
[![CircleCI branch](https://img.shields.io/circleci/project/Sagacify/komitet-gita-bezopasnosti/master.svg?maxAge=2592000)](https://circleci.com/gh/Sagacify/komitet-gita-bezopasnosti/tree/master)
[![Docker Stars](https://img.shields.io/docker/stars/sagacify/kgb.svg?maxAge=2592000)](https://hub.docker.com/r/sagacify/kgb/)

Комитет Git'a Безопасности (КGБ)  or Git security committee, is a commit message style enforcer.
It comes in two parts, a web hook for github (lubyanka) and a local git commit-msg hook (resident).
In an ideal world, a local hook should be enough, in practice, mistakes happen.
The KGitB is here to ensure no mistakes are ever allowed through to infect your master branch.

examples
--------
* [failing](https://github.com/Sagacify/komitet-gita-bezopasnosti/pull/4)
* [passing](https://github.com/Sagacify/komitet-gita-bezopasnosti/pull/6)


# resident
Resident can be installed using pip using the following command. If you have a permission errors try using the --user flag with pip and add ~/.local/bin to your path. It should not require any dependencies.
```
pip install kgitb
```

To install in a local repository, go into it and run:
```
resident install --local
```

To set it up in another repository or multiple repository, you can path it a path to the repositor(y/ies) that you want to install it to:
```
resident install --path PATH_TO_REPO1 PATH_TO_REPO2
```

To set it up globally.

WARNING 0: Only works with git 2.9.0+

WARNING1: If it hasn't been set yet, this option will set the core.hooksPath value in your ```.gitconfig``` to ```$HOME/.config/git-global-hooks```. This will disable all local hooks in your repositories. If this is not what you want, you might want to have a look at hook templates.

WARNING2: global means for the user, system setup hasn't been implemented (yet, PR anyone?).

```
resident install --global
```

If the webhook is correctly set up, you should see a ```APPROVED BY THE KGitB.``` line when you commit something, or if there are errors, the commit will fail with a description of the errors.

Currently there are no options to select. They will be added at a later point.

# lubyanka
Lubyanka is the headquarters of all residents.
It should be run on a server and setup with github to check all pull-requests.
As excpected, if there are any violations, lubyanka will submit a helpful if somewhat authoritative comment message and set the status to error.
If there are no violations it will set the status to success and congragulate you on a job well done.

To run lubyanka, get a copy of the code, install the requirements and execute it with the following commands:
```
git clone https://github.com/Sagacify/komitet-gita-bezopasnosti.git
cd komitet-gita-bezopasnosti
pip install -r requirements.txt
GH_TOKEN=`YOUR GITHUB TOKEN HERE` python -m kgitb
```


If you use docker remember to set the GH_TOKEN environment variable and link to port 5000.

The github token is needed to write comments, set the pr status as well as access any private repo.

# Contribute
All contributions are of course welcome, please submit them as pull-requests and make sure that you are not in violation of the kgitb rules.
If you need ideas:
* Add rules list and documentation
* resident, add --template, --template--system and --system install
* resident, add lubyanka command line options for customizing rules
* lubyanka, add origin of connection check [cfr](https://github.com/carlos-jenkins/python-github-webhooks/blob/master/webhooks.py#L56)
* lubyanka, add setup script
* packaging, figure out how extra_requires works.

to test your changes please use tox and py.test, you should be able to install them by running:
```
pip install -r dev-requirements.txt
````

and run the tests using:
```
tox
````

# Publish
* generate README.rst
```
pandoc --from=markdown --to=rst --output=README.rst README.md
```
* publish
```
python setup.py sdist upload
```
