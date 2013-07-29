===================================
tld
===================================

Description
===================================
Extracts the top level domain (TLD) from the URL given. List of TLD names is taken from
Mozilla http://mxr.mozilla.org/mozilla/source/netwerk/dns/src/effective_tld_names.dat?raw=1

Optionally raises exceptions on non-existing TLDs or silently fails (if `fail_silently` argument is set to True).
Knows about active and inactive TLDs. If only active TLDs shall be matched against, `active_only` argument shall be
set to True (default - False).

Installation
===================================
Latest stable version on PyPI:

    $ pip install tld

Latest development version:

    $ pip install -e hg+http://bitbucket.org/barseghyanartur/tld#egg=tld

Usage example
===================================
To get the top level domain name from the URL given:

    >>> from tld import get_tld
    >>> print get_tld("http://www.google.co.uk")
    'google.co.uk'
    >>> print get_tld("http://www.google.idontexist", fail_silently=True)
    None

To update/sync the tld names with the most recent version run the following from your terminal:

    $ python tld/update.py

    or simply do:

    >>> from tld.utils import update_tld_names
    >>> update_tld_names()

License
===================================
MPL 1.1/GPL 2.0/LGPL 2.1

Support
===================================
For any issues contact me at the e-mail given in the `Author` section.

Author
===================================
Artur Barseghyan <artur.barseghyan@gmail.com>
