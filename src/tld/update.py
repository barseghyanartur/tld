from __future__ import print_function

"""
Deprecated. Use ``update-tld-names`` command instead.
"""

__title__ = 'tld.update'
__author__ = 'Artur Barseghyan'
__copyright__ = '2013-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'

from tld.utils import update_tld_names

_ = lambda x: x

if __name__ == '__main__':
    update_tld_names()
    print(_("Local TLD names file has been successfully updated!"))

