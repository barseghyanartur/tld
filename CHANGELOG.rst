Release history and notes
=========================
`Sequence based identifiers
<http://en.wikipedia.org/wiki/Software_versioning#Sequence-based_identifiers>`_
are used for versioning (schema follows below):

.. code-block:: none

    major.minor[.revision]

- It's always safe to upgrade within the same minor version (for example, from
  0.3 to 0.3.4).
- Minor version changes might be backwards incompatible. Read the
  release notes carefully before upgrading (for example, when upgrading from
  0.3.4 to 0.4).
- All backwards incompatible changes are mentioned in this document.

0.8
---
2018-mm-dd (not yet released).

- Move to a Trie to match TLDs. This brings a speed up of 15-20%.
- It's now possible to search in public, private or all suffixes (old
  behaviour). Use `search_public` and `search_private` arguments accordingly.
  By default (to support old behavior), both are set to True.
- Domains like `*****.xn--fiqs8s` are now recognized as well.
- Due to usage of `urlsplit` instead of `urlparse`, the initial list of TLDs
  is assembled quicker (a speed-up of 15-20%).
- Docs/ directory is included in source distribution tarball.

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
