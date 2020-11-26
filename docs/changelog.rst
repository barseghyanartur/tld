Release history and notes
=========================
`Sequence based identifiers
<http://en.wikipedia.org/wiki/Software_versioning#Sequence-based_identifiers>`_
are used for versioning (schema follows below):

.. code-block:: text

    major.minor[.revision]

- It's always safe to upgrade within the same minor version (for example, from
  0.3 to 0.3.4).
- Minor version changes might be backwards incompatible. Read the
  release notes carefully before upgrading (for example, when upgrading from
  0.3.4 to 0.4).
- All backwards incompatible changes are mentioned in this document.

0.12.3
------
2020-11-26

- Separate parsers for (a) public and private and (b) public only domains. This
  fixes a bug. If you want an old behaviour:

  The following code would raise exception in past.

  .. code-block:: python

    from tld import get_tld

    get_tld(
        'http://silly.cc.ua',
        search_private=False
    )

  Now it would return `ua`.

  .. code-block:: python

    get_tld(
        'http://silly.cc.ua',
        search_private=False
    )

  If you want old behavior, do as follows:

  .. code-block:: python

    from tld.utils import MozillaTLDSourceParser

    get_tld(
        'http://silly.cc.ua',
        search_private=False,
        parser_class=MozillaTLDSourceParser
    )

  Same goes for ``get_fld``, ``process_url``, ``parse_tld`` and ``is_tld``
  functions.

0.12.2
------
2020-05-20

- Add mozilla license to dist.
- Fix MyPy issues.

0.12.1
------
2020-04-25

.. note::

    In commemoration of `Armenian Genocide <https://en.wikipedia.org/wiki/Armenian_Genocide>`_.

- Correctly handling domain names ending with dot(s).

0.12
----
2020-04-19

- Use Public Suffix list instead of deprecated Mozilla's MXR.

0.11.11
------
2020-03-10

- Minor speed-ups, reduce memory usage.

0.11.10
------
2020-02-05

- Python 2.7 and 3.5 fixes.

0.11.9
------
2019-12-16

- Adding test TLDs list to the package.

0.11.8
------
2019-12-13

- Minor fixes in setup.py.

0.11.7
------
2019-12-13

.. note::

    There have been no code changes since 0.11.2. The only change is that
    support for Python 2.7 and 3.5 has been added.

- Added support for Python 2.7.

0.11.6
------
2019-12-12

- Targeted releases for all supported Python versions.

0.11.5
------
2019-12-12

- Targeted releases for all supported Python versions.

0.11.4
------
2019-12-12

- Changed order of the releases (Python 3.6 and up come first, then Python 3.5).
- Make all distributions except Python 3.5 universal.

0.11.3
------
2019-12-12

- Added missing resources to the Python 3.5 release.

0.11.2
------
2019-12-12

- Bring back Python 3.5 support.

0.11.1
----
2019-12-11

- Minor speed ups.
- More on adding typing.

0.11
----
2019-12-09

.. note::

    Since introduction of parser classes, usage of
    ``NAMES_SOURCE_URL`` and ``NAMES_LOCAL_PATH`` of the ``tld.conf``
    module is deprecated. Also, ``tld_names_local_path``
    and ``tld_names_source_url`` arguments are deprecated as well.
    If you want to customise things, implement your own parser (inherit from
    ``BaseTLDSourceParser``).

- Drop support for Python versions prior to 3.6.
- Clean-up dependencies.
- Introduce parsers.
- Drop ``tld_names_source_url`` and ``tld_names_local_path`` introduced
  in the previous release.
- Minor speed-ups (including tests).

0.10
----
2019-11-27

.. note::

    This is the last release to support Python 2.

- Make it possible to provide a custom path to the TLD names file.
- Make it possible to free up some resources occupied due to loading custom
  tld names by calling the ``reset_tld_names`` function
  with ``tld_names_local_path`` parameter.

0.9.8
-----
2019-11-15

- Fix for occasional issue when some domains are not correctly recognised.

0.9.7
-----
2019-10-30

.. note::

    This release is dedicated to my newborn daughter. Happy birthday, my dear
    Ani.

- Handling urls that are only a TLD.
- Accepts already splitted URLs.
- Tested against Python 3.8.

0.9.6
-----
2019-09-12

- Fix for update-tld-names returns a non-zero exit code on success (introduced
  with optimisations in 0.9.4).
- Minor tests improvements.

0.9.5
-----
2019-09-11

- Tests improvements.

0.9.4
-----
2019-09-11

- Optimisations in setup.py, tests and console scripts.
- Skip testing the update-tld-names functionality if no internet is available.

0.9.3
-----
2019-04-05

- Added `is_tld` function.
- Docs updated.
- Upgrade test suite.

0.9.2
-----
2019-01-10

- Fix an issue causing certain punycode TLDs to be deemed invalid.
- Tested against Python 3.7.
- Added tests for commands.
- Dropped Python 2.6 support.
- TLD source updated to the latest version.

0.9.1
-----
2018-07-09

- Correctly handling nested TLDs.

0.9
---
2018-06-14

.. note::

    This release contains backward incompatible changes. You should update
    your code.

    The ``active_only`` option has been removed from ``get_tld``, ``get_fld``
    and ``parse_url`` functions. Update your code accordingly.

- Removed ``active_only`` option from ``get_tld``, ``get_fld``
  and ``parse_url`` functions.
- Correctly handling exceptions (!) in the original TLD list.
- Fixes in documentation.
- Added ``parse_tld`` function.
- Fixes the ``python setup.py test`` command.

0.8
---
2018-06-13

.. note::

    This release contains backward incompatible changes. You should update
    your code.

    Old ``get_tld`` functionality is moved to ``get_fld`` (first-level
    domain definition). The ``as_object`` argument (False by default) has been
    deprecated for ``get_fld``.

    .. code-block:: python

        res = get_tld("http://www.google.co.uk", as_object=True)

    **Old behaviour**

    .. code-block:: text

        In: res.domain
        Out: 'google'

        In: res.extension
        Out: 'co.uk'

        In: res.subdomain
        Out: 'www'

        In: res.suffix
        Out: 'co.uk'

        In: res.tld
        Out: 'google.co.uk'

    **New behaviour**

    .. code-block:: text

        In: res.fld
        Out: 'google.co.uk'

        In: res.tld
        Out: 'co.uk'

        In: res.domain
        Out: 'google'

        In: res.subdomain
        Out: 'www'

    When used without ``as_object`` it returns ``co.uk``.

    **Recap**

    If you have been happily using old version of ``get_tld`` function without
    ``as_object`` argument set to ``True``, you might want to replace ``get_tld``
    import with ``get_fld`` import:

    .. code-block:: python

        # Old
        from tld import get_tld
        get_tld('http://google.co.uk')

        # New
        from tld import get_fld
        get_fld('http://google.co.uk')

- Move to a Trie to match TLDs. This brings a speed up of 15-20%.
- It's now possible to search in public, private or all suffixes (old
  behaviour). Use ``search_public`` and ``search_private`` arguments accordingly.
  By default (to support old behavior), both are set to True.
- Correct TLD definitions.
- Domains like `*****.xn--fiqs8s` are now recognized as well.
- Due to usage of ``urlsplit`` instead of ``urlparse``, the initial list of TLDs
  is assembled quicker (a speed-up of 15-20%).
- Docs/ directory is included in source distribution tarball.
- More tests.

0.7.10
------
2018-04-07

- The ``fix_protocol`` argument respects protocol relative URLs.
- Change year in the license.
- Improved docstrings.
- TLD source updated to the latest version.

0.7.9
-----
2017-05-02

- Added base path override for local .dat file.
- `python setup.py test` can used to execute the tests

0.7.8
-----
2017-02-19

- Fix relative import in non-package for update-tls-names script. #15
- ``get_tld`` got a new argument ``fix_protocol``, which fixes the missing
  protocol, having prepended "https" if missing or incorrect.

0.7.7
-----
2017-02-09

- Tested against Python 3.5, 3.6 and PyPy.
- pep8 fixes.
- removed deprecated `tld.update` module. Use ``update-tld-names`` command
  instead.

0.7.6
-----
2016-01-23

- Minor fixes.

0.7.5
-----
2015-11-22

- Minor fixes.
- Updated tld names file to the latest version.

0.7.4
-----
2015-09-24

- Exposed TLD initialization as ``get_tld_names``.

0.7.3
-----
2015-07-18

- Support for wheel packages.
- Fixed failure on some unicode domains.
- TLD source updated to the latest version.
- Documentation updated.

0.7.2
-----
2014-09-28

- Minor fixes.

0.7.1
-----
2014-09-23

- Force lower case of the URL for correct search.

0.7
---
2014-08-14

- Making it possible to obtain object instead of just extracting the TLD by
  setting the ``as_object`` argument of ``get_tld`` function to True.

0.6.4
-----
2014-05-21

- Softened dependencies and lowered the ``six`` package version requirement to
  1.4.0.
- Documentation improvements.

0.6.3
-----
2013-12-05

- Speed up search

0.6.2
-----
2013-12-03

- Fix for URLs with a port not handled correctly.
- Adding licenses.

0.6.1
-----
2013-09-15

- Minor fixes.
- Credits added.

0.6
---
2013-09-12

- Fixes for Python 3 (Windows encoding).

0.5
---
2013-09-13

- Python 3 support added.

0.4
---
2013-08-03

- Tiny code improvements.
- Tests added.
