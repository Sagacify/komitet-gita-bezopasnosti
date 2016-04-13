Komitet Git'a Bezopasnosti
==========================
.. image:: https://circleci.com/gh/Sagacify/komitet-gita-bezopasnosti.svg?style=svg
    :target: https://circleci.com/gh/Sagacify/komitet-gita-bezopasnosti

Komitet Git'a Bezopasnosti (kgb) or Git security committee, is a commit 
message style enforcer.
It will listen to pull-request(pr) events from github, analyse the
commit messages in the pr, and if there are any violations, 
it will submit a helpful if somewhat authoritative comment message and 
set the status to error.
If there are no violations it will set the status to success.

If you want to run it you can use:

.. code-block:: bash

    $ GH_TOKEN=`YOUR GITHUB TOKEN HERE` python -m komitet_git_bezopasnosti

If you use docker remember to set the GH_TOKEN environment variable and
link to port 5000.

The github token is needed to write comments, set the pr status as
well as access any private repo.


examples
--------
* failing_
* passing_

.. _failing: https://github.com/Sagacify/komitet-gita-bezopasnosti/pull/4
.. _passing: https://github.com/Sagacify/komitet-gita-bezopasnosti/pull/6
