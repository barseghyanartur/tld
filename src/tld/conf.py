__title__ = 'tld.conf'
__version__ = '0.3'
__build__ = 0x000003
__author__ = 'Artur Barseghyan'
__all__ = ('get_setting', 'settings',)

class Settings(object):
    def __init__(self):
        self._settings = {
            # Source path of Mozilla's effective TLD names file.
            'NAMES_SOURCE_URL': 'http://mxr.mozilla.org/mozilla/source/netwerk/dns/src/effective_tld_names.dat?raw=1',

            # Relative path to store the local copy of Mozilla's effective TLD names file.
            'NAMES_LOCAL_PATH': 'res/effective_tld_names.dat.txt',

            # Debug flag.
            'DEBUG': False
        }

    def set(name, value):
        self._settings[name] = value

    def get(self, name, default=None):
        if self._settings.has_key(name):
            return self._settings[name]
        else:
            return default

settings = Settings()

get_setting = settings.get
