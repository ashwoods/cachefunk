Cachefunk: Sitemap cache warmer
===============================

.. image:: https://img.shields.io/pypi/v/cachefunk.svg
    :target: https://pypi.python.org/pypi/cachefunk
    :alt: PyPi page link -- version

.. image:: https://img.shields.io/pypi/l/cachefunk.svg
    :target: https://pypi.python.org/pypi/cachefunk
    :alt: PyPi page link -- MIT licence

.. image:: https://img.shields.io/pypi/pyversions/cachefunk.svg
    :target: https://pypi.python.org/pypi/cachefunk
    :alt: PyPi page link -- Python versions

.. image:: https://img.shields.io/travis/ashwoods/cachefunk.svg
    :target: https://travis-ci.org/ashwoods/cachefunk
    :alt: Travis CI Status

.. image:: https://img.shields.io/coveralls/ashwoods/cachefunk/master.svg
    :target: https://coveralls.io/r/ashwoods/cachefunk
    :alt: Coverage status

.. image:: https://api.codacy.com/project/badge/Grade/e2f906fa26b44ce2b539c22b6d5be333
    :target: https://www.codacy.com/app/ashwoods/cachefunk?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ashwoods/cachefunk&amp;utm_campaign=Badge_Grade
    :alt: Codacy link

.. image:: https://codeclimate.com/github/ashwoods/cachefunk/badges/gpa.svg
   :target: https://codeclimate.com/github/codeclimate/codeclimate
   :alt: Code Climate

In theory, cachefunk is just a simple cache warming command line tool that can fetch a list of URLs from sitemap.xml
and make a GET request on each url. In practise this is just a tool for me to play around with async
python libraries.


Installation
------------

To install the current version:

.. code-block:: bash

    $ pip install cachefunk


Usage
-----

.. code-block:: bash

    $ cachefunk --url https://example.com/sitemap.xml  run

    $ cachefunk --help
    Usage: cachefunk [OPTIONS] COMMAND [ARGS]...

    Options:
      -v, --verbosity LVL     Either CRITICAL, ERROR, WARNING, INFO or DEBUG
      --url TEXT              Sitemap.xml URL
      -c, --concurrent TEXT   Enable concurrency
      --timeout INTEGER       Request timeout
      --verify-ssl TEXT       Enable SSL verification
      --verify-response TEXT  Verify the response
      --force-https TEXT      Force https
      --replace TEXT          Replace url base
      --progress TEXT         Show progress
      --help                  Show this message and exit.

    Commands:
      dryrun
      run


Features
--------

TODO: :)



Using cachefunk from python
---------------------------

You can also use cachefunk from python. Docs to come, but the `cachefunk.funk.Funk` class is pretty straight forward.




