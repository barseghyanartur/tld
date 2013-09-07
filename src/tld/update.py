__title__ = 'tld.update'
__version__ = '0.5'
__build__ = 0x000005
__author__ = 'Artur Barseghyan'

from six import print_

from tld.utils import update_tld_names

_ = lambda x: x

if __name__ == '__main__':
    update_tld_names()
    print_(_("Local TLD names file has been successfully updated!"))
