__title__ = 'tld.update'
__version__ = '0.3'
__build__ = 0x000003
__author__ = 'Artur Barseghyan'

from tld.utils import update_tld_names

_ = lambda x: x

if __name__ == '__main__':
    update_tld_names()
    print _("Local TLD names file has been successfully updated!")
