__title__ = 'tld.conf'
__version__ = '0.5'
__build__ = 0x000005
__author__ = 'Artur Barseghyan'
__all__ = ('get_setting', 'set_setting', 'settings',)

from tld import defaults

class Settings(object):
    """
    Settings registry.
    """
    def __init__(self):
        self._settings = {}

    def set(self, name, value):
        """
        Override default settings.

        :param str name:
        :param mixed value:
        """
        self._settings[name] = value

    def get(self, name, default=None):
        """
        Gets a variable from local settings.

        :param str name:
        :param mixed default: Default value.
        :return mixed:
        """
        if name in self._settings:
            return self._settings.get(name, default)
        elif hasattr(defaults, name):
            return getattr(defaults, name, default)
        else:
            return default

settings = Settings()

get_setting = settings.get

set_setting = settings.set
