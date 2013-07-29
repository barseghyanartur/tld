__title__ = 'tld.settings'
__version__ = '0.3'
__build__ = 0x000003
__author__ = 'Artur Barseghyan'
__all__ = ('NAMES_SOURCE_URL', 'NAMES_LOCAL_PATH', 'DEBUG')

from tld.conf import get_setting

NAMES_SOURCE_URL = get_setting('NAMES_SOURCE_URL')

NAMES_LOCAL_PATH = get_setting('NAMES_LOCAL_PATH')

DEBUG = get_setting('DEBUG')
