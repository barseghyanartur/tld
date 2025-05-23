===
tld
===
Extract the top level domain (TLD) from the URL given. List of TLD names is
taken from `Public Suffix <https://publicsuffix.org/list/public_suffix_list.dat>`_.

Optionally raises exceptions on non-existing TLDs or silently fails (if
``fail_silently`` argument is set to True).

.. image:: https://img.shields.io/pypi/v/tld.svg
   :target: https://pypi.python.org/pypi/tld
   :alt: PyPI Version

.. image:: https://img.shields.io/pypi/pyversions/tld.svg
    :target: https://pypi.python.org/pypi/tld/
    :alt: Supported Python versions

.. image:: https://github.com/barseghyanartur/tld/workflows/test/badge.svg
   :target: https://github.com/barseghyanartur/tld/actions
   :alt: Build Status

.. image:: https://readthedocs.org/projects/tld/badge/?version=latest
    :target: http://tld.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://img.shields.io/badge/docs-llms.txt-blue
    :target: http://tld.readthedocs.io/en/latest/llms.txt
    :alt: llms.txt - documentation for LLMs

.. image:: https://img.shields.io/badge/license-MPL--1.1%20OR%20GPL--2.0--only%20OR%20LGPL--2.1--or--later-blue.svg
   :target: https://github.com/barseghyanartur/tld/#License
   :alt: MPL-1.1 OR GPL-2.0-only OR LGPL-2.1-or-later

.. image:: https://coveralls.io/repos/github/barseghyanartur/tld/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/barseghyanartur/tld?branch=master
    :alt: Coverage

Prerequisites
=============
- Python 3.9 or greater.

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

Usage examples
==============
In addition to examples below, see the `jupyter notebook <jupyter/>`_
workbook file.

Get the TLD name **as string** from the URL given
-------------------------------------------------
.. code-block:: python
    :name: test_get_tld_name_as_string_from_url_given

    from tld import get_tld

    get_tld("http://www.google.co.uk")
    # 'co.uk'

    get_tld("http://www.google.idontexist", fail_silently=True)
    # None

Get the TLD as **an object**
----------------------------
.. code-block:: python
    :name: test_get_tld_name_as_an_object

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
    :name: test_get_tld_name_ignoring_the_missing_protocol

    from tld import get_tld, get_fld

    get_tld("www.google.co.uk", fix_protocol=True)
    # 'co.uk'

    get_fld("www.google.co.uk", fix_protocol=True)
    # 'google.co.uk'

Return TLD parts as tuple
-------------------------
.. code-block:: python
    :name: test_get_tld_parts_as_tuple

    from tld import parse_tld

    parse_tld('http://www.google.com')
    # 'com', 'google', 'www'

Get the first level domain name **as string** from the URL given
----------------------------------------------------------------
.. code-block:: python
    :name: test_get_first_level_domain_name_as_string_from_url_given

    from tld import get_fld

    get_fld("http://www.google.co.uk")
    # 'google.co.uk'

    get_fld("http://www.google.idontexist", fail_silently=True)
    # None

Check if some tld is a valid tld
--------------------------------

.. code-block:: python
    :name: test_check_if_some_tld_is_a_valid_tld

    from tld import is_tld

    is_tld('co.uk')
    # True

    is_tld('uk')
    # True

    is_tld('tld.doesnotexist')
    # False

    is_tld('www.google.com')
    # False

Update the list of TLD names
============================
To update/sync the tld names with the most recent versions run the following
from your terminal:

.. code-block:: sh

    update-tld-names

Or simply do:

.. code-block:: python
    :name: test_update_the_list_of_tld_names

    from tld.utils import update_tld_names

    update_tld_names()

Note, that this will update all registered TLD source parsers (not only the
list of TLD names taken from Mozilla). In order to run the update for a single
parser, append ``uid`` of that parser as argument.

.. code-block:: sh

    update-tld-names mozilla

Custom TLD parsers
==================
By default list of TLD names is taken from Mozilla. Parsing implemented in
the ``tld.utils.MozillaTLDSourceParser`` class. If you want to use another
parser, subclass the ``tld.base.BaseTLDSourceParser``, provide ``uid``,
``source_url``, ``local_path`` and implement the ``get_tld_names`` method.
Take the ``tld.utils.MozillaTLDSourceParser`` as a good example of such
implementation. You could then use ``get_tld`` (as well as other ``tld``
module functions) as shown below:

.. code-block:: python

    from tld import get_tld
    from some.module import CustomTLDSourceParser

    get_tld(
        "http://www.google.co.uk",
        parser_class=CustomTLDSourceParser
    )

Custom list of TLD names
========================
You could maintain your own custom version of the TLD names list (even multiple
ones) and use them simultaneously with built in TLD names list.

You would then store them locally and provide a path to it as shown below:

.. code-block:: python
    :name: test_get_tld_custom_list_of_tld_names

    from tld import get_tld
    from tld.utils import BaseMozillaTLDSourceParser

    class CustomBaseMozillaTLDSourceParser(BaseMozillaTLDSourceParser):

        uid: str = 'custom_mozilla'
        local_path: str = 'tests/res/effective_tld_names_custom.dat.txt'

    get_tld(
        "http://www.foreverchild",
        parser_class=CustomBaseMozillaTLDSourceParser
    )
    # 'foreverchild'

Same goes for first level domain names:

.. continue: test_get_tld_custom_list_of_tld_names
.. code-block:: python
    :name: test_get_fld_custom_list_of_tld_names

    from tld import get_fld

    get_fld(
        "http://www.foreverchild",
        parser_class=CustomBaseMozillaTLDSourceParser
    )
    # 'www.foreverchild'

Note, that in both examples shown above, there the original TLD names file has
been modified in the following way:

.. code-block:: text

    ...
    // ===BEGIN ICANN DOMAINS===

    // This one actually does not exist, added for testing purposes
    foreverchild
    ...

Free up resources
=================
To free up memory occupied by loading of custom TLD names, use
``reset_tld_names`` function with ``tld_names_local_path`` parameter.

.. continue: test_get_tld_custom_list_of_tld_names
.. code-block:: python
    :name: test_free_up_resources

    from tld import get_tld, reset_tld_names

    # Get TLD from a custom TLD names parser
    get_tld(
        "http://www.foreverchild",
        parser_class=CustomBaseMozillaTLDSourceParser
    )

    # Free resources occupied by the custom TLD names list
    reset_tld_names("tests/res/effective_tld_names_custom.dat.txt")

Troubleshooting
===============
If somehow domain names listed `here <https://publicsuffix.org/list/public_suffix_list.dat>`_
are not recognised, make sure you have the most recent version of TLD names in
your virtual environment:

.. code-block:: sh

    update-tld-names

To update TLD names list for a single parser, specify it as an argument:

.. code-block:: sh

    update-tld-names mozilla

Testing
=======
Simply type:

.. code-block:: sh

    pytest

Or use tox:

.. code-block:: sh

    tox

Or use tox to check specific env:

.. code-block:: sh

    tox -e py39

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
For security issues contact me at the e-mail given in the `Author`_ section.

For overall issues, go to `GitHub <https://github.com/barseghyanartur/tld/issues>`_.

Author
======
Artur Barseghyan <artur.barseghyan@gmail.com>
