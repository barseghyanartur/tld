__title__ = 'tld.settings'
__version__ = '0.5'
__build__ = 0x000005
__author__ = 'Artur Barseghyan'
__all__ = ('NAMES_SOURCE_URL', 'NAMES_LOCAL_PATH', 'DEBUG')

import warnings
warnings.warn("""tld.settings is deprecated; use tld.conf.get_setting function instead.""",
              DeprecationWarning)

from tld.conf import get_setting

NAMES_SOURCE_URL = get_setting('NAMES_SOURCE_URL')

NAMES_LOCAL_PATH = get_setting('NAMES_LOCAL_PATH')

DEBUG = get_setting('DEBUG')
