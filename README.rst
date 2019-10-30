===
tld
===
Extract the top level domain (TLD) from the URL given. List of TLD names is
taken from `Mozilla
<http://mxr.mozilla.org/mozilla/source/netwerk/dns/src/effective_tld_names.dat?raw=1>`_.

Optionally raises exceptions on non-existing TLDs or silently fails (if
``fail_silently`` argument is set to True).

.. image:: https://img.shields.io/pypi/v/tld.svg
   :target: https://pypi.python.org/pypi/tld
   :alt: PyPI Version

.. image:: https://img.shields.io/pypi/pyversions/tld.svg
    :target: https://pypi.python.org/pypi/tld/
    :alt: Supported Python versions

.. image:: https://img.shields.io/travis/barseghyanartur/tld/master.svg
   :target: http://travis-ci.org/barseghyanartur/tld
   :alt: Build Status

.. image:: https://img.shields.io/badge/license-MPL--1.1%20OR%20GPL--2.0--only%20OR%20LGPL--2.1--or--later-blue.svg
   :target: https://github.com/barseghyanartur/tld/#License
   :alt: MPL-1.1 OR GPL-2.0-only OR LGPL-2.1-or-later

.. image:: https://coveralls.io/repos/github/barseghyanartur/tld/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/barseghyanartur/tld?branch=master
    :alt: Coverage

Prerequisites
=============
- Python 2.7, 3.4, 3.5, 3.6, 3.7, 3.8 and PyPy

Documentation
=============
Documentation is available on `Read the Docs
<http://tld.readthedocs.io/>`_.

Installation
============
Latest stable version on PyPI:

.. code-block:: sh

    pip install tld

Or latest stable version from GitHub:

.. code-block:: sh

    pip install https://github.com/barseghyanartur/tld/archive/stable.tar.gz

Or latest stable version from BitBucket:

.. code-block:: sh

    pip install https://bitbucket.org/barseghyanartur/tld/get/stable.tar.gz

Usage examples
==============
In addition to examples below, see the `jupyter notebook <jupyter/>`_
workbook file.

Get the TLD name **as string** from the URL given
-------------------------------------------------
.. code-block:: python

    from tld import get_tld

    get_tld("http://www.google.co.uk")
    # 'co.uk'

    get_tld("http://www.google.idontexist", fail_silently=True)
    # None

Get the TLD as **an object**
----------------------------
.. code-block:: python

    from tld import get_tld

    res = get_tld("http://some.subdomain.google.co.uk", as_object=True)

    res
    # 'co.uk'

    res.subdomain
    # 'some.subdomain'

    res.domain
    # 'google'

    res.tld
    # 'co.uk'

    res.fld
    # 'google.co.uk'

    res.parsed_url
    # SplitResult(
    #     scheme='http',
    #     netloc='some.subdomain.google.co.uk',
    #     path='',
    #     query='',
    #     fragment=''
    # )

Get TLD name, **ignoring the missing protocol**
-----------------------------------------------
.. code-block:: python

    from tld import get_tld, get_fld

    get_tld("www.google.co.uk", fix_protocol=True)
    # 'co.uk'

    get_fld("www.google.co.uk", fix_protocol=True)
    # 'google.co.uk'

Return TLD parts as tuple
-------------------------
.. code-block:: python

    from tld import parse_tld

    parse_tld('http://www.google.com')
    # 'com', 'google', 'www'

Get the first level domain name **as string** from the URL given
----------------------------------------------------------------
.. code-block:: python

    from tld import get_fld

    get_fld("http://www.google.co.uk")
    # 'google.co.uk'

    get_fld("http://www.google.idontexist", fail_silently=True)
    # None

Check if some tld is a valid tld
--------------------------------

.. code-block:: python

    from tld import is_tld

    is_tld('co.uk)
    # True

    is_tld('uk')
    # True

    is_tld('tld.doesnotexist')
    # False

    is_tld('www.google.com')
    # False

Update the list of TLD names
============================
To update/sync the tld names with the most recent version run the following
from your terminal:

.. code-block:: sh

    update-tld-names

Or simply do:

.. code-block:: python

    from tld.utils import update_tld_names

    update_tld_names()

Troubleshooting
===============
If somehow domain names listed `here
<http://mxr.mozilla.org/mozilla/source/netwerk/dns/src/effective_tld_names.dat?raw=1>`_
are not recognised, make sure you have the most recent version of TLD names in
your virtual environment:

.. code-block:: sh

    update-tld-names

Testing
=======
Simply type:

.. code-block:: sh

    ./runtests.py

Or use tox:

.. code-block:: sh

    tox

Or use tox to check specific env:

.. code-block:: sh

    tox -e py36

Writing documentation
=====================

Keep the following hierarchy.

.. code-block:: text

    =====
    title
    =====

    header
    ======

    sub-header
    ----------

    sub-sub-header
    ~~~~~~~~~~~~~~

    sub-sub-sub-header
    ^^^^^^^^^^^^^^^^^^

    sub-sub-sub-sub-header
    ++++++++++++++++++++++

    sub-sub-sub-sub-sub-header
    **************************

License
=======
MPL-1.1 OR GPL-2.0-only OR LGPL-2.1-or-later

Support
=======
For any issues contact me at the e-mail given in the `Author`_ section.

Author
======
Artur Barseghyan <artur.barseghyan@gmail.com>
