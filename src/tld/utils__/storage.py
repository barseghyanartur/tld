from __future__ import unicode_literals
import argparse
from codecs import open as codecs_open
from functools import lru_cache
# codecs_open = open
from os.path import isabs
import sys
from typing import Dict, Type, Union, Tuple, List, Optional
from urllib.parse import urlsplit, SplitResult

from ..base import BaseTLDSourceParser
from ..exceptions import (
    TldBadUrl,
    TldDomainNotFound,
    TldImproperlyConfigured,
    TldIOError,
)
from ..helpers import project_dir
from ..trie import Trie
from ..registry import Registry
from ..result import Result

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

tld_names: Dict[str, Trie] = {}


def get_tld_names_container() -> Dict[str, Trie]:
    """Get container of all tld names.

    :return:
    :rtype dict:
    """
    global tld_names
    return tld_names


def update_tld_names_container(tld_names_local_path: str,
                               trie_obj: Trie) -> None:
    """Update TLD Names container item.

    :param tld_names_local_path:
    :param trie_obj:
    :return:
    """
    global tld_names
    # tld_names.update({tld_names_local_path: trie_obj})
    tld_names[tld_names_local_path] = trie_obj


def pop_tld_names_container(tld_names_local_path: str) -> None:
    """Remove TLD names container item.

    :param tld_names_local_path:
    :return:
    """
    global tld_names
    tld_names.pop(tld_names_local_path, None)


@lru_cache(maxsize=128, typed=True)
def update_tld_names(
    fail_silently: bool = False,
    parser_uid: str = None
) -> bool:
    """Update TLD names.

    :param fail_silently:
    :param parser_uid:
    :return:
    """
    results: List[bool] = []
    results_append = results.append
    if parser_uid:
        parser_cls = Registry.get(parser_uid, None)
        if parser_cls and parser_cls.source_url:
            results_append(
                parser_cls.update_tld_names(fail_silently=fail_silently)
            )
    else:
        for parser_uid, parser_cls in Registry.items():
            if parser_cls and parser_cls.source_url:
                results_append(
                    parser_cls.update_tld_names(fail_silently=fail_silently)
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
    parser.add_argument(
        '--fail-silently',
        dest="fail_silently",
        default=False,
        action='store_true',
        help="Fail silently",
    )
    args = parser.parse_args(sys.argv[1:])
    parser_uid = args.parser_uid
    fail_silently = args.fail_silently
    return int(
        not update_tld_names(
            parser_uid=parser_uid,
            fail_silently=fail_silently
        )
    )


def get_tld_names(
    fail_silently: bool = False,
    retry_count: int = 0,
    parser_class: Type[BaseTLDSourceParser] = None
) -> Dict[str, Trie]:
    """Build the ``tlds`` list if empty. Recursive.

    :param fail_silently: If set to True, no exceptions are raised and None
        is returned on failure.
    :param retry_count: If greater than 1, we raise an exception in order
        to avoid infinite loops.
    :param parser_class:
    :type fail_silently: bool
    :type retry_count: int
    :type parser_class: BaseTLDSourceParser
    :return: List of TLD names
    :rtype: obj:`tld.utils.Trie`
    """
    if not parser_class:
        parser_class = MozillaTLDSourceParser

    return parser_class.get_tld_names(
        fail_silently=fail_silently,
        retry_count=retry_count
    )