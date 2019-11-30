import codecs

from urllib.request import urlopen

from .exceptions import (
    TldIOError,
    TldImproperlyConfigured,
)
from .helpers import project_dir
from .registry import Registry

__author__ = 'Artur Barseghyan'
__copyright__ = '2013-2019 Artur Barseghyan'
__license__ = 'MPL-1.1 OR GPL-2.0-only OR LGPL-2.0-or-later'
__all__ = ('BaseTLDSourceParser',)


class BaseTLDSourceParser(metaclass=Registry):
    """Base TLD source parser."""

    uid: str = None
    source_url: str = None
    local_path: str = None

    def __init__(self,
                 source_url: str = None,
                 local_path: str = None):
        """Constructor.

        :param source_url:
        :param local_path:
        """
        if source_url:
            self.source_url = source_url

        if local_path:
            self.local_path = local_path

        if not self.uid:
            raise TldImproperlyConfigured(
                "The `uid` property of the TLD source parser shall be defined."
            )

    def get_tld_names(self, fail_silently: bool = False, retry_count: int = 0):
        """Get tld names.

        :param fail_silently:
        :param retry_count:
        :return:
        """
        raise NotImplementedError(
            "Your TLD source parser shall implement `get_tld_names` method."
        )

    def update_tld_names(self, fail_silently: bool = False) -> bool:
        """Update the local copy of the TLD file.

        :param fail_silently:
        :return:
        """
        try:
            remote_file = urlopen(self.source_url)
            local_file = codecs.open(
                project_dir(self.local_path),
                'wb',
                encoding='utf8'
            )
            local_file.write(remote_file.read().decode('utf8'))
            local_file.close()
            remote_file.close()
        except Exception as err:
            if fail_silently:
                return False
            raise TldIOError(err)

        return True
