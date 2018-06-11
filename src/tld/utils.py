from __future__ import unicode_literals

import codecs

from six import PY3, text_type
from six.moves.urllib.parse import urlparse
from six.moves.urllib.request import urlopen

from .conf import get_setting
from .exceptions import TldIOError, TldDomainNotFound, TldBadUrl
from .helpers import project_dir

__title__ = 'tld.utils'
__author__ = 'Artur Barseghyan'
__copyright__ = '2013-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'get_tld',
    'get_tld_names',
    'Result',
    'update_tld_names',
)

tld_names = None


class Result(object):
    """Container."""

    __slots__ = ('subdomain', 'domain', 'suffix', '__tld')

    def __init__(self, subdomain, domain, suffix):
        self.subdomain = subdomain
        self.domain = domain
        self.suffix = suffix
        self.__tld = "{0}.{1}".format(self.domain, self.suffix)

    @property
    def tld(self):
        """TLD."""
        return self.__tld

    @property
    def extension(self):
        """Alias of ``suffix``.

        :return str:
        """
        return self.suffix

    def __unicode__(self):
        if PY3:
            return self.__tld
        else:
            try:
                return self.__tld.encode('utf8')
            except UnicodeEncodeError:
                return self.__tld
    __repr__ = __unicode__
    __str__ = __unicode__


class TrieNode(object):
    """Class representing a single Trie node."""

    __slots__ = ('children', 'leaf', 'private')

    def __init__(self):
        self.children = None
        self.leaf = False
        self.private = False


class Trie(object):
    """An adhoc Trie data structure to store tlds in reverse notation order."""

    def __init__(self):
        self.root = TrieNode()
        self.__nodes = 0

    def __len__(self):
        return self.__nodes

    def add(self, tld, private=False):
        node = self.root

        # Iterating over the tld parts in reverse order
        for part in reversed(tld.split('.')):

            # To save up some RAM, we initialize the children dict only
            # when strictly necessary
            if node.children is None:
                node.children = {}

            child = node.children.get(part)

            if child is None:
                child = TrieNode()

            node.children[part] = child

            node = child

        node.leaf = True

        if private:
            node.private = True

        self.__nodes += 1


def update_tld_names(fail_silently=False):
    """Update the local copy of TLDs file.

    :param fail_silently: If set to True, no exceptions is raised on
        failure but boolean False returned.
    :type fail_silently: bool
    :return: True on success, False on failure.
    :rtype: bool
    """
    tld_names_source_url = get_setting('NAMES_SOURCE_URL')
    tld_names_local_path = get_setting('NAMES_LOCAL_PATH')
    try:
        remote_file = urlopen(tld_names_source_url)
        local_file = codecs.open(
            project_dir(tld_names_local_path),
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


def get_tld_names(fail_silently=False, retry_count=0):
    """Build the ``tlds`` list if empty. Recursive.

    :param fail_silently: If set to True, no exceptions are raised and None
        is returned on failure.
    :param retry_count: If greater than 1, we raise an exception in order
        to avoid infinite loops.
    :type fail_silently: bool
    :type retry_count: int
    :return: List of TLD names
    :type: iterable
    """
    tld_names_local_path = get_setting('NAMES_LOCAL_PATH')

    if retry_count > 1:
        if fail_silently:
            return None
        else:
            raise TldIOError

    global tld_names

    # If already loaded, return
    if tld_names is not None:
        return tld_names

    local_file = None
    try:
        # Load the TLD names file
        local_file = codecs.open(project_dir(tld_names_local_path),
                                 'r',
                                 encoding='utf8')
        tld_names = Trie()
        # Make a list of it all, strip all garbage
        private_section = False

        for line in local_file:
            if '===BEGIN PRIVATE DOMAINS===' in line:
                private_section = True

            # Puny code tlds
            if '// xn--' in line:
                line = line.split(' (', 1)[0][3:]

            if line[0] == '/' or line[0] == '\n':
                continue

            tld_names.add(u'{0}'.format(line.strip()), private=private_section)

        local_file.close()
    except IOError as err:
        update_tld_names()  # Grab the file
        # Increment ``retry_count`` in order to avoid infinite loops
        retry_count += 1
        return get_tld_names(fail_silently, retry_count)  # Run again
    except Exception as err:
        try:
            local_file.close()
        except Exception:
            pass

        if fail_silently:
            return None
        else:
            raise err

    return tld_names


def get_tld(url,
            active_only=False,
            fail_silently=False,
            as_object=False,
            fix_protocol=False,
            search_public=True,
            search_private=True):
    """Extract the top level domain.

    Extract the top level domain based on the mozilla's effective TLD names
    dat file. Returns a string. May throw ``TldBadUrl`` or
    ``TldDomainNotFound`` exceptions if there's bad URL provided or no TLD
    match found respectively.

    :param url: URL to get top level domain from.
    :param active_only: If set to True, only active patterns are matched.
    :param fail_silently: If set to True, no exceptions are raised and None
        is returned on failure.
    :param as_object: If set to True, ``tld.utils.Result`` object is returned,
        ``domain``, ``suffix`` and ``tld`` properties.
    :param fix_protocol: If set to True, missing or wrong protocol is
        ignored (https is appended instead).
    :type url: str
    :type active_only: bool
    :type fail_silently: bool
    :type as_object: bool
    :type fix_protocol: bool
    :type search_public: bool
    :type search_private: bool
    :return: String with top level domain (if ``as_object`` argument
        is set to False) or a ``tld.utils.Result`` object (if ``as_object``
        argument is set to True); returns None on failure.
    :rtype: str
    """
    url = url.lower()

    if fix_protocol:
        if (
            not url.startswith('//')
            and not (url.startswith('http://') or url.startswith('https://'))
        ):
            url = 'https://{}'.format(url)

    tld_names = get_tld_names(fail_silently=fail_silently)  # Init

    # Get (sub) domain name
    domain_name = urlparse(url).netloc.split(":", 1)[0]

    if not domain_name:
        if fail_silently:
            return None
        else:
            raise TldBadUrl(url=url)

    domain_parts = domain_name.split('.')

    # Now we query our Trie iterating on the domain parts in reverse order
    node = tld_names.root
    tld_length = 0
    for i in reversed(range(len(domain_parts))):
        part = domain_parts[i]

        # Cannot go deeper
        if node.children is None:
            break

        child = node.children.get(part)

        # Wildcards
        if child is None:
            child = node.children.get('*')

        # Inactive
        if active_only is False and child is None:
            child = node.children.get('!{0}'.format(part))

        # If the current part is not in current node's children, we can stop
        if child is None:
            break

        # Else we move deeper and increment our tld offset
        tld_length += 1
        node = child

    # Checking the node we finished on is a leaf and is one we allow
    if (
        (not node.leaf) or
        (not search_public and not node.private) or
        (not search_private and node.private)
    ):
        if fail_silently:
            return None
        else:
            raise TldDomainNotFound(domain_name=domain_name)

    non_zero_i = max(1, len(domain_parts) - tld_length)

    if not as_object:
        return text_type(".").join(domain_parts[non_zero_i-1:])

    subdomain = text_type(".").join(domain_parts[:non_zero_i-1])
    domain = text_type(".").join(
        domain_parts[non_zero_i-1:non_zero_i]
    )
    suffix = text_type(".").join(domain_parts[non_zero_i:])

    return Result(subdomain, domain, suffix)
