from __future__ import unicode_literals
import argparse
import codecs
import sys
from typing import Dict, Type, Union, Tuple
from urllib.parse import urlsplit, SplitResult

from .conf import get_setting
from .base import BaseTLDSourceParser
from .exceptions import (
    TldBadUrl,
    TldDomainNotFound,
    TldImproperlyConfigured,
    TldIOError,
)
from .helpers import project_dir
from .trie import Trie
from .registry import REGISTRY
from .result import Result

__author__ = 'Artur Barseghyan'
__copyright__ = '2013-2019 Artur Barseghyan'
__license__ = 'MPL-1.1 OR GPL-2.0-only OR LGPL-2.0-or-later'
__all__ = (
    'get_fld',
    'get_tld',
    'get_tld_names',
    'get_tld_names_container',
    'update_tld_names_container',
    'pop_tld_names_container',
    'is_tld',
    'parse_tld',
    'process_url',
    'reset_tld_names',
    'Result',
    'update_tld_names',
    'update_tld_names_cli',
)

tld_names: Dict[str, Trie] = {}


def get_tld_names_container() -> Dict[str, Trie]:
    """Get container of all tld names.

    :return:
    :rtype dict:
    """
    global tld_names
    return tld_names


def update_tld_names_container(tld_names_local_path: str,
                               trie_obj: Trie) -> Type[None]:
    """Update TLD Names container item.

    :param tld_names_local_path:
    :param trie_obj:
    :return:
    """
    global tld_names
    tld_names.update({tld_names_local_path: trie_obj})


def pop_tld_names_container(tld_names_local_path: str) -> Type[None]:
    """Remove TLD names container item.

    :param tld_names_local_path:
    :return:
    """
    global tld_names
    tld_names.pop(tld_names_local_path, None)


# Already implemented in `BaseTLDSourceParser.update_tld_names`
# def update_tld_names(fail_silently: bool = False,
#                      tld_names_source_url: str = None,
#                      tld_names_local_path: str = None) -> bool:
#     """Update the local copy of TLDs file.
#
#     :param fail_silently: If set to True, no exceptions is raised on
#         failure but boolean False returned.
#     :param tld_names_source_url:
#     :param tld_names_local_path:
#     :type fail_silently: bool
#     :type tld_names_source_url: str
#     :type tld_names_local_path: str
#     :return: True on success, False on failure.
#     :rtype: bool
#     """
#     if not tld_names_source_url:
#         tld_names_source_url = get_setting('NAMES_SOURCE_URL', None)
#
#     if not tld_names_local_path:
#         tld_names_local_path = get_setting('NAMES_LOCAL_PATH', None)
#
#     try:
#         remote_file = urlopen(tld_names_source_url)
#         local_file = codecs.open(
#             project_dir(tld_names_local_path),
#             'wb',
#             encoding='utf8'
#         )
#         local_file.write(remote_file.read().decode('utf8'))
#         local_file.close()
#         remote_file.close()
#     except Exception as err:
#         if fail_silently:
#             return False
#         raise TldIOError(err)
#
#     return True


def update_tld_names(
    fail_silently: bool = False,
    tld_names_source_url: str = None,
    tld_names_local_path: str = None,
    parser_uid: str = None
) -> bool:
    """Update TLD names.

    :param fail_silently:
    :param parser_uid:
    :return:
    """
    results = []
    if parser_uid:
        parser_cls = REGISTRY.get(parser_uid, None)
        if parser_cls and parser_cls.source_url:
            if not tld_names_source_url:
                tld_names_source_url = get_setting('NAMES_SOURCE_URL', None)

            if not tld_names_local_path:
                tld_names_local_path = get_setting('NAMES_LOCAL_PATH', None)
            parser = parser_cls(
                source_url=tld_names_source_url,
                local_path=tld_names_local_path
            )
            results.append(
                parser.update_tld_names(fail_silently=fail_silently)
            )
    else:
        for parser_uid, parser_cls in REGISTRY.items():
            if parser_cls and parser_cls.source_url:
                parser = parser_cls()
                results.append(
                    parser.update_tld_names(fail_silently=fail_silently)
                )

    return all(results)


def update_tld_names_cli() -> int:
    """CLI wrapper for update_tld_names.

    Since update_tld_names returns True on success, we need to negate the
    result to match CLI semantics.
    """
    parser = argparse.ArgumentParser(description='Update TLD names')
    parser.add_argument(
        'parser_uid',
        nargs='?',
        default=None,
        help="UID of the parser to update TLD names for.",
    )
    args = parser.parse_args(sys.argv[1:])
    parser_uid = args.parser_uid
    return int(not update_tld_names(parser_uid=parser_uid))


def get_tld_names(
    fail_silently: bool = False,
    retry_count: int = 0,
    tld_names_source_url: str = None,
    tld_names_local_path: str = None,
    parser_class: BaseTLDSourceParser = None
) -> Dict[str, Trie]:
    """Build the ``tlds`` list if empty. Recursive.

    :param fail_silently: If set to True, no exceptions are raised and None
        is returned on failure.
    :param retry_count: If greater than 1, we raise an exception in order
        to avoid infinite loops.
    :param tld_names_source_url:
    :param tld_names_local_path:
    :param parser_class:
    :type fail_silently: bool
    :type retry_count: int
    :type tld_names_local_path: str
    :type parser_class: BaseTLDSourceParser
    :return: List of TLD names
    :rtype: obj:`tld.utils.Trie`
    """
    if not tld_names_source_url:
        tld_names_source_url = get_setting('NAMES_SOURCE_URL', None)

    if not tld_names_local_path:
        tld_names_local_path = get_setting('NAMES_LOCAL_PATH', None)

    if not parser_class:
        parser_class = MozillaTLDSourceParser

    parser = parser_class(
        source_url=tld_names_source_url,
        local_path=tld_names_local_path
    )
    return parser.get_tld_names(
        fail_silently=fail_silently,
        retry_count=retry_count
    )


def process_url(
    url: str,
    fail_silently: bool = False,
    fix_protocol: bool = False,
    search_public: bool = True,
    search_private: bool = True,
    tld_names_source_url: str = None,
    tld_names_local_path: str = None,
    parser_class: BaseTLDSourceParser = None
):
    """Process URL.

    :param parser_class:
    :param url:
    :param fail_silently:
    :param fix_protocol:
    :param search_public:
    :param search_private:
    :param tld_names_source_url:
    :param tld_names_local_path:
    :return:
    """
    if not (search_public or search_private):
        raise TldImproperlyConfigured(
            "Either `search_public` or `search_private` (or both) shall be "
            "set to True."
        )

    if not tld_names_local_path:
        tld_names_source_url = get_setting('NAMES_SOURCE_URL', None)

    if not tld_names_local_path:
        tld_names_local_path = get_setting('NAMES_LOCAL_PATH', None)

    # Init
    _tld_names = get_tld_names(
        fail_silently=fail_silently,
        tld_names_source_url=tld_names_source_url,
        tld_names_local_path=tld_names_local_path,
        parser_class=parser_class
    )

    if not isinstance(url, SplitResult):
        url = url.lower()

        if fix_protocol:
            if (
                not url.startswith('//')
                and not (
                    url.startswith('http://') or url.startswith('https://')
                )
            ):
                url = 'https://{}'.format(url)

        # Get parsed URL as we might need it later
        parsed_url = urlsplit(url)
    else:
        parsed_url = url

    # Get (sub) domain name
    domain_name = parsed_url.hostname

    if not domain_name:
        if fail_silently:
            return None, None, parsed_url
        else:
            raise TldBadUrl(url=url)

    domain_parts = domain_name.split('.')

    # Now we query our Trie iterating on the domain parts in reverse order
    node = _tld_names[tld_names_local_path].root
    current_length = 0
    tld_length = 0
    match = None
    for i in reversed(range(len(domain_parts))):
        part = domain_parts[i]

        # Cannot go deeper
        if node.children is None:
            break

        # Exception
        if part == node.exception:
            break

        child = node.children.get(part)

        # Wildcards
        if child is None:
            child = node.children.get('*')

        # If the current part is not in current node's children, we can stop
        if child is None:
            break

        # Else we move deeper and increment our tld offset
        current_length += 1
        node = child

        if node.leaf:
            tld_length = current_length
            match = node

    # Checking the node we finished on is a leaf and is one we allow
    if (
        (match is None) or
        (not match.leaf) or
        (not search_public and not match.private) or
        (not search_private and match.private)
    ):
        if fail_silently:
            return None, None, parsed_url
        else:
            raise TldDomainNotFound(domain_name=domain_name)

    if len(domain_parts) == tld_length:
        non_zero_i = -1  # hostname = tld
    else:
        non_zero_i = max(1, len(domain_parts) - tld_length)

    return domain_parts, non_zero_i, parsed_url


def get_fld(
    url: str,
    fail_silently: bool = False,
    fix_protocol: bool = False,
    search_public: bool = True,
    search_private: bool = True,
    tld_names_source_url: str = None,
    tld_names_local_path: str = None,
    parser_class: BaseTLDSourceParser = None,
    **kwargs
) -> Union[str, Type[None]]:
    """Extract the first level domain.

    Extract the top level domain based on the mozilla's effective TLD names
    dat file. Returns a string. May throw ``TldBadUrl`` or
    ``TldDomainNotFound`` exceptions if there's bad URL provided or no TLD
    match found respectively.

    :param url: URL to get top level domain from.
    :param fail_silently: If set to True, no exceptions are raised and None
        is returned on failure.
    :param fix_protocol: If set to True, missing or wrong protocol is
        ignored (https is appended instead).
    :param search_public: If set to True, search in public domains.
    :param search_private: If set to True, search in private domains.
    :param tld_names_source_url:
    :param tld_names_local_path:
    :param parser_class:
    :type url: str
    :type fail_silently: bool
    :type fix_protocol: bool
    :type search_public: bool
    :type search_private: bool
    :type tld_names_local_path: str
    :return: String with top level domain (if ``as_object`` argument
        is set to False) or a ``tld.utils.Result`` object (if ``as_object``
        argument is set to True); returns None on failure.
    :rtype: str
    """
    if 'as_object' in kwargs:
        raise TldImproperlyConfigured(
            "`as_object` argument is deprecated for `get_fld`. Use `get_tld` "
            "instead."
        )

    domain_parts, non_zero_i, parsed_url = process_url(
        url=url,
        fail_silently=fail_silently,
        fix_protocol=fix_protocol,
        search_public=search_public,
        search_private=search_private,
        tld_names_source_url=tld_names_source_url,
        tld_names_local_path=tld_names_local_path,
        parser_class=parser_class
    )

    if domain_parts is None:
        return None

    if non_zero_i < 0:
        # hostname = tld
        return str(parsed_url.hostname)

    return str(".").join(domain_parts[non_zero_i-1:])


def get_tld(
    url: str,
    fail_silently: bool = False,
    as_object: bool = False,
    fix_protocol: bool = False,
    search_public: bool = True,
    search_private: bool = True,
    tld_names_source_url: str = None,
    tld_names_local_path: str = None,
    parser_class: BaseTLDSourceParser = None
) -> Union[Type[None], str, Result]:
    """Extract the top level domain.

    Extract the top level domain based on the mozilla's effective TLD names
    dat file. Returns a string. May throw ``TldBadUrl`` or
    ``TldDomainNotFound`` exceptions if there's bad URL provided or no TLD
    match found respectively.

    :param url: URL to get top level domain from.
    :param fail_silently: If set to True, no exceptions are raised and None
        is returned on failure.
    :param as_object: If set to True, ``tld.utils.Result`` object is returned,
        ``domain``, ``suffix`` and ``tld`` properties.
    :param fix_protocol: If set to True, missing or wrong protocol is
        ignored (https is appended instead).
    :param search_public: If set to True, search in public domains.
    :param search_private: If set to True, search in private domains.
    :param tld_names_source_url:
    :param tld_names_local_path:
    :param parser_class:
    :type url: str
    :type fail_silently: bool
    :type as_object: bool
    :type fix_protocol: bool
    :type search_public: bool
    :type search_private: bool
    :type tld_names_local_path: str
    :return: String with top level domain (if ``as_object`` argument
        is set to False) or a ``tld.utils.Result`` object (if ``as_object``
        argument is set to True); returns None on failure.
    :rtype: str
    """
    domain_parts, non_zero_i, parsed_url = process_url(
        url=url,
        fail_silently=fail_silently,
        fix_protocol=fix_protocol,
        search_public=search_public,
        search_private=search_private,
        tld_names_source_url=tld_names_source_url,
        tld_names_local_path=tld_names_local_path,
        parser_class=parser_class
    )

    if domain_parts is None:
        return None

    if not as_object:
        if non_zero_i < 0:
            # hostname = tld
            return str(parsed_url.hostname)
        return str(".").join(domain_parts[non_zero_i:])

    if non_zero_i < 0:
        # hostname = tld
        subdomain = str("")
        domain = str("")
        _tld = str(parsed_url.hostname)
    else:
        subdomain = str(".").join(domain_parts[:non_zero_i-1])
        domain = str(".").join(
            domain_parts[non_zero_i-1:non_zero_i]
        )
        _tld = str(".").join(domain_parts[non_zero_i:])

    return Result(
        subdomain=subdomain,
        domain=domain,
        tld=_tld,
        parsed_url=parsed_url
    )


def parse_tld(
    url: str,
    fail_silently=False,
    fix_protocol=False,
    search_public=True,
    search_private=True,
    tld_names_source_url: str = None,
    tld_names_local_path: str = None,
    parser_class: BaseTLDSourceParser = None
) -> Union[Tuple[Type[None], Type[None], Type[None]], Tuple[str, str, str]]:
    """Parse TLD into parts.

    :param url:
    :param fail_silently:
    :param fix_protocol:
    :param search_public:
    :param search_private:
    :param tld_names_source_url:
    :param tld_names_local_path:
    :param parser_class:
    :return:
    :rtype: tuple
    """
    try:
        obj = get_tld(
            url,
            fail_silently=fail_silently,
            as_object=True,
            fix_protocol=fix_protocol,
            search_public=search_public,
            search_private=search_private,
            tld_names_source_url=tld_names_source_url,
            tld_names_local_path=tld_names_local_path,
            parser_class=parser_class
        )
        _tld = obj.tld
        domain = obj.domain
        subdomain = obj.subdomain

    except (
        TldBadUrl,
        TldDomainNotFound,
        TldImproperlyConfigured,
        TldIOError
    ):
        _tld = None
        domain = None
        subdomain = None

    return _tld, domain, subdomain


def is_tld(
    value: str,
    search_public: bool = True,
    search_private: bool = True,
    tld_names_source_url: str = None,
    tld_names_local_path: str = None,
    parser_class: BaseTLDSourceParser = None
) -> bool:
    """Check if given URL is tld.

    :param value: URL to get top level domain from.
    :param search_public: If set to True, search in public domains.
    :param search_private: If set to True, search in private domains.
    :param tld_names_source_url:
    :param tld_names_local_path:
    :param parser_class:
    :type value: str
    :type search_public: bool
    :type search_private: bool
    :type tld_names_local_path: str
    :return:
    :rtype: bool
    """
    _tld = get_tld(
        url=value,
        fail_silently=True,
        fix_protocol=True,
        search_public=search_public,
        search_private=search_private,
        tld_names_source_url=tld_names_source_url,
        tld_names_local_path=tld_names_local_path,
        parser_class=parser_class
    )
    return value == _tld


def reset_tld_names(tld_names_local_path: str = None) -> Type[None]:
    """Reset the ``tld_names`` to empty value.

    If ``tld_names_local_path`` is given, removes specified
    entry from ``tld_names`` instead.

    :param tld_names_local_path:
    :type tld_names_local_path: str
    :return:
    """

    if tld_names_local_path:
        pop_tld_names_container(tld_names_local_path)
    else:
        global tld_names
        tld_names = {}


# **************************************************************************
# **************************** Parser classes ******************************
# **************************************************************************

class MozillaTLDSourceParser(BaseTLDSourceParser):
    """Mozilla TLD source."""

    uid = 'mozilla'
    source_url = 'http://mxr.mozilla.org/mozilla/source/netwerk/dns/src/' \
                 'effective_tld_names.dat?raw=1'
    local_path = 'res/effective_tld_names.dat.txt'

    def get_tld_names(self,
                      fail_silently: bool = False,
                      retry_count: int = 0) -> Dict[str, Trie]:
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

        # global tld_names
        _tld_names = get_tld_names_container()

        # # If already loaded, return
        # if (
        #         self.local_path in tld_names
        #         and tld_names[self.local_path] is not None
        # ):
        #     return tld_names

        # If already loaded, return
        if (
            self.local_path in _tld_names
            and _tld_names[self.local_path] is not None
        ):
            return _tld_names

        local_file = None
        try:
            # Load the TLD names file
            local_file = codecs.open(
                project_dir(self.local_path),
                'r',
                encoding='utf8'
            )
            trie = Trie()
            # Make a list of it all, strip all garbage
            private_section = False

            for line in local_file:
                if '===BEGIN PRIVATE DOMAINS===' in line:
                    private_section = True

                # Puny code TLD names
                if '// xn--' in line:
                    line = line.split()[1]

                if line[0] == '/' or line[0] == '\n':
                    continue

                trie.add(
                    u'{0}'.format(line.strip()),
                    private=private_section
                )

            # tld_names[self.local_path] = trie
            update_tld_names_container(self.local_path, trie)

            local_file.close()
        except IOError as err:
            # Grab the file
            self.update_tld_names(
                fail_silently=fail_silently
            )
            # Increment ``retry_count`` in order to avoid infinite loops
            retry_count += 1
            # Run again
            return self.get_tld_names(
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

        # return tld_names
        return _tld_names
