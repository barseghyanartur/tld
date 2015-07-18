===
tld
===
Extracts the top level domain (TLD) from the URL given. List of TLD names is
taken from `Mozilla
<http://mxr.mozilla.org/mozilla/source/netwerk/dns/src/effective_tld_names.dat?raw=1>`_.

Optionally raises exceptions on non-existing TLDs or silently fails (if
`fail_silently` argument is set to True). Knows about active and inactive TLDs.
If only active TLDs shall be matched against, `active_only` argument shall be
set to True (default - False).

Installation
============
Latest stable version on PyPI:

.. code-block:: none

    $ pip install tld

Latest development version:

.. code-block:: none

    $ pip install -e hg+http://bitbucket.org/barseghyanartur/tld#egg=tld

Usage example
=============
To get the top level domain name from the URL given:

.. code-block:: python

    from tld import get_tld
    print get_tld("http://www.google.co.uk")
    # 'google.co.uk'

    print get_tld("http://www.google.idontexist", fail_silently=True)
    # None

If you wish, you could get the result as an object:

.. code-block:: python

    from tld import get_tld
    res = get_tld("http://some.subdomain.google.co.uk", as_object=True)
    print res
    # 'google.co.uk'

    print res.subdomain
    # 'some.subdomain'

    print res.domain
    # 'google'

    print res.suffix
    # 'co.uk'

    print res.tld
    # 'google.co.uk'

To update/sync the tld names with the most recent version run the following
from your terminal:

.. code-block:: none

    $ update-tld-names

or simply do:

.. code-block:: python

    from tld.utils import update_tld_names
    update_tld_names()

Troubleshooting
===============
If somehow domain names listed `here
<http://mxr.mozilla.org/mozilla/source/netwerk/dns/src/effective_tld_names.dat?raw=1>`_
are not recognised, make sure you have the most recent version of TLD names in
your virtual environment:

.. code-block:: none

    $ update-tld-names

License
=======
MPL 1.1/GPL 2.0/LGPL 2.1

Support
=======
For any issues contact me at the e-mail given in the `Author` section.

Author
======
Artur Barseghyan <artur.barseghyan@gmail.com>
