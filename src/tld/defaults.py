__title__ = 'tld.defaults'
__author__ = 'Artur Barseghyan'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('NAMES_SOURCE_URL', 'NAMES_LOCAL_PATH', 'DEBUG')

# Source path of Mozilla's effective TLD names file.
NAMES_SOURCE_URL = 'http://mxr.mozilla.org/mozilla/source/netwerk/dns/src/effective_tld_names.dat?raw=1'

# Relative path to store the local copy of Mozilla's effective TLD names file.
NAMES_LOCAL_PATH =  'res/effective_tld_names.dat.txt'

DEBUG = False
