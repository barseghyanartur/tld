__title__ = 'tld.defaults'
__version__ = '0.6'
__build__ = 0x000006
__author__ = 'Artur Barseghyan'
__all__ = ('NAMES_SOURCE_URL', 'NAMES_LOCAL_PATH', 'DEBUG')

# Source path of Mozilla's effective TLD names file.
NAMES_SOURCE_URL = 'http://mxr.mozilla.org/mozilla/source/netwerk/dns/src/effective_tld_names.dat?raw=1'

# Relative path to store the local copy of Mozilla's effective TLD names file.
NAMES_LOCAL_PATH =  'res/effective_tld_names.dat.txt'

DEBUG = False
