from . import defaults

__title__ = 'tld.conf'
__author__ = 'Artur Barseghyan'
__copyright__ = '2013-2019 Artur Barseghyan'
__license__ = 'MPL-1.1 OR GPL-2.0-only OR LGPL-2.0-or-later'
__all__ = (
    'get_setting',
    'reset_settings',
    'set_setting',
    'settings',
)


class Settings(object):
    """Settings registry."""

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

        return default

    def reset(self):
        """Reset settings."""
        for name in defaults.__all__:
            self.set(name, getattr(defaults, name))


settings = Settings()

get_setting = settings.get

set_setting = settings.set

reset_settings = settings.reset
