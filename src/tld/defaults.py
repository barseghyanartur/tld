import os

__title__ = 'tld.defaults'
__author__ = 'Artur Barseghyan'
__copyright__ = '2013-2019 Artur Barseghyan'
__license__ = 'MPL-1.1 OR GPL-2.0-only OR LGPL-2.0-or-later'
__all__ = (
    'DEBUG',
    'NAMES_LOCAL_PATH',
    'NAMES_LOCAL_PATH_PARENT',
    'NAMES_SOURCE_URL',
)

# Source path of Mozilla's effective TLD names file.
NAMES_SOURCE_URL = 'http://mxr.mozilla.org/mozilla/source/netwerk/dns/src/' \
                   'effective_tld_names.dat?raw=1'

# Relative path to store the local copy of Mozilla's effective TLD names file.
NAMES_LOCAL_PATH = 'res/effective_tld_names.dat.txt'

# Absolute base path that is prepended to NAMES_LOCAL_PATH
NAMES_LOCAL_PATH_PARENT = os.path.dirname(__file__)

DEBUG = False
