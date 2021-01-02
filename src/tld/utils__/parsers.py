from __future__ import unicode_literals
import argparse
from codecs import open as codecs_open
from functools import lru_cache
# codecs_open = open
from os.path import isabs
import sys
from typing import Dict, Type, Union, Tuple, List, Optional
from urllib.parse import urlsplit, SplitResult

from .base import BaseTLDSourceParser
from .exceptions import (
    TldBadUrl,
    TldDomainNotFound,
    TldImproperlyConfigured,
    TldIOError,
)
from .helpers import project_dir
from .trie import Trie
from .registry import Registry
from .result import Result

__author__ = 'Artur Barseghyan'
__copyright__ = '2013-2020 Artur Barseghyan'
__license__ = 'MPL-1.1 OR GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = (
    'BaseMozillaTLDSourceParser',
    'get_fld',
    'get_tld',
    'get_tld_names',
    'get_tld_names_container',
    'is_tld',
    'MozillaTLDSourceParser',
    'MozillaPublicOnlyTLDSourceParser',
    'parse_tld',
    'pop_tld_names_container',
    'process_url',
    'reset_tld_names',
    'Result',
    'tld_names',
    'update_tld_names',
    'update_tld_names_cli',
    'update_tld_names_container',
)


# **************************************************************************
# **************************** Parser classes ******************************
# **************************************************************************

class BaseMozillaTLDSourceParser(BaseTLDSourceParser):

    @classmethod
    def get_tld_names(
        cls,
        fail_silently: bool = False,
        retry_count: int = 0
    ) -> Optional[Dict[str, Trie]]:
        """Parse.

        :param fail_silently:
        :param retry_count:
        :return:
        """
        if retry_count > 1:
            if fail_silently:
                return None
            else:
                raise TldIOError

        global tld_names
        _tld_names = tld_names
        # _tld_names = get_tld_names_container()

        # If already loaded, return
        if (
            cls.local_path in _tld_names
            and _tld_names[cls.local_path] is not None
        ):
            return _tld_names

        try:
            # Load the TLD names file
            if isabs(cls.local_path):
                local_path = cls.local_path
            else:
                local_path = project_dir(cls.local_path)
            local_file = codecs_open(
                local_path,
                'r',
                encoding='utf8'
            )
            trie = Trie()
            trie_add = trie.add  # Performance opt
            # Make a list of it all, strip all garbage
            private_section = False
            include_private = cls.include_private

            for line in local_file:
                if '===BEGIN PRIVATE DOMAINS===' in line:
                    private_section = True

                if private_section and not include_private:
                    break

                # Puny code TLD names
                if '// xn--' in line:
                    line = line.split()[1]

                if line[0] in ('/', '\n'):
                    continue

                trie_add(
                    f'{line.strip()}',
                    private=private_section
                )

            update_tld_names_container(cls.local_path, trie)

            local_file.close()
        except IOError as err:
            # Grab the file
            cls.update_tld_names(
                fail_silently=fail_silently
            )
            # Increment ``retry_count`` in order to avoid infinite loops
            retry_count += 1
            # Run again
            return cls.get_tld_names(
                fail_silently=fail_silently,
                retry_count=retry_count
            )
        except Exception as err:
            if fail_silently:
                return None
            else:
                raise err
        finally:
            try:
                local_file.close()
            except Exception:
                pass

        return _tld_names


class MozillaTLDSourceParser(BaseMozillaTLDSourceParser):
    """Mozilla TLD source."""

    uid: str = 'mozilla'
    source_url: str = 'https://publicsuffix.org/list/public_suffix_list.dat'
    local_path: str = 'res/effective_tld_names.dat.txt'


class MozillaPublicOnlyTLDSourceParser(BaseMozillaTLDSourceParser):
    """Mozilla TLD source."""

    uid: str = 'mozilla_public_only'
    source_url: str = 'https://publicsuffix.org/list/public_suffix_list.dat' \
                      '?publiconly'
    local_path: str = 'res/effective_tld_names_public_only.dat.txt'
    include_private: bool = False

