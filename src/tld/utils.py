from __future__ import unicode_literals

__title__ = 'tld.utils'
__author__ = 'Artur Barseghyan'
__copyright__ = '2013-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('update_tld_names', 'get_tld_names', 'get_tld', 'Result',)

import os
import codecs

from six import PY3
from six.moves.urllib.parse import urlparse
from six.moves.urllib.request import urlopen
from six import text_type

from tld.conf import get_setting
from tld.exceptions import TldIOError, TldDomainNotFound, TldBadUrl

PROJECT_DIR = lambda base : os.path.abspath(os.path.join(os.path.dirname(__file__), base).replace('\\','/'))

_ = lambda x: x

tld_names = []


class Result(object):
    """
    Container.
    """
    __slots__ = ('subdomain', 'domain', 'suffix', '__tld')

    def __init__(self, subdomain, domain, suffix):
        self.subdomain = subdomain
        self.domain = domain
        self.suffix = suffix
        self.__tld = "{0}.{1}".format(self.domain, self.suffix)

    @property
    def tld(self):
        return self.__tld

    @property
    def extension(self):
        """
        Alias of ``suffix``.

        :return str:
        """
        return self.suffix

    def __unicode__(self):
        if PY3:
            return self.__tld
        else:
            try:
                return self.__tld.encode('utf8')
            except UnicodeEncodeError as err:
                return self.__tld
    __repr__ = __unicode__
    __str__ = __unicode__


def update_tld_names(fail_silently=False):
    """
    Updates the local copy of TLDs file.

    :param bool fail_silently: If set to True, no exceptions is raised on
        failure but boolean False returned.
    :return bool: True on success, False on failure.
    """
    TLD_NAMES_SOURCE_URL = get_setting('NAMES_SOURCE_URL')
    TLD_NAMES_LOCAL_PATH = get_setting('NAMES_LOCAL_PATH')
    try:
        remote_file = urlopen(TLD_NAMES_SOURCE_URL)
        local_file = codecs.open(PROJECT_DIR(TLD_NAMES_LOCAL_PATH),
                                 'wb',
                                 encoding='utf8')
        local_file.write(remote_file.read().decode('utf8'))
        local_file.close()
        remote_file.close()
    except Exception as err:
        if fail_silently:
            return False
        raise TldIOError(err)

    return True


def get_tld_names(fail_silently=False, retry_count=0):
    """
    Build the ``tlds`` list if empty. Recursive.

    :param fail_silently: If set to True, no exceptions are raised and None
        is returned on failure.
    :param retry_count: If greater than 1, we raise an exception in order
        to avoid infinite loops.
    :return: Returns interable
    """
    TLD_NAMES_LOCAL_PATH = get_setting('NAMES_LOCAL_PATH')

    if retry_count > 1:
        if fail_silently:
            return None
        else:
            raise TldIOError

    global tld_names

    # If already loaded, return
    if len(tld_names):
        return tld_names

    local_file = None
    try:
        # Load the TLD names file
        local_file = codecs.open(PROJECT_DIR(TLD_NAMES_LOCAL_PATH),
                                 'r',
                                 encoding='utf8')
        # Make a list of it all, strip all garbage
        tld_names = set([u'{0}'.format(line.strip()) for line \
                         in local_file if line[0] not in '/\n'])
        local_file.close()
    except IOError as err:
        update_tld_names() # Grab the file
        retry_count += 1 # Increment ``retry_count`` in order to avoid
                         # infinite loops
        return init(retry_count) # Run again
    except Exception as err:
        try:
            local_file.close()
        except:
            pass

        if fail_silently:
            return None
        else:
            raise err

    return tld_names


def get_tld(url, active_only=False, fail_silently=False, as_object=False):
    """
    Extracts the top level domain based on the mozilla's effective TLD names
    dat file. Returns a string. May throw ``TldBadUrl`` or
    ``TldDomainNotFound`` exceptions if there's bad URL provided or no TLD
    match found respectively.

    :param url: URL to get top level domain from.
    :param active_only: If set to True, only active patterns are matched.
    :param fail_silently: If set to True, no exceptions are raised and None
        is returned on failure.
    :param as_object: If set to True, ``tld.utils.Result`` object is returned,
        ``domain``, ``suffix`` and ``tld`` properties.
    :return mixed: String with top level domain (if ``as_object`` argument
        is set to False) or a ``tld.utils.Result`` object (if ``as_object``
        argument is set to True); returns None on failure.
    """

    url = url.lower()

    tld_names = get_tld_names(fail_silently=fail_silently) # Init

    # Get (sub) domain name
    domain_name = urlparse(url).netloc.split(":", 1)[0]

    if not domain_name:
        if fail_silently:
            return None
        else:
            raise TldBadUrl(url=url)

    domain_parts = domain_name.split('.')

    # Looping from much to less (for example if we have a domain named
    # "v3.api.google.co.uk" we'll try "v3.api.google.co.uk", then
    # "api.google.co.uk", then "api.google.co.uk", then "google.co.uk", then
    # "co.uk" and finally "uk". If the last one does not match any TLDs, we
    # throw a <TldDomainNotFound> exception.
    for i in range(0, len(domain_parts)):
        sliced_domain_parts = domain_parts[i:]

        match = text_type('.').join(sliced_domain_parts)
        wildcard_match = text_type('.').join(['*'] + sliced_domain_parts[1:])
        inactive_match = text_type("!{0}").format(match)

        #if not PY3:
        #    try:
        #        match = match.encode('utf8')
        #        wildcard_match = wildcard_match.encode('utf8')
        #        inactive_match = inactive_match.encode('utf8')
        #    except UnicodeDecodeError as e:
        #        pass

        # Match tlds
        if (match in tld_names or wildcard_match in tld_names or (active_only is False and inactive_match in tld_names)):
            if not as_object:
                return text_type(".").join(domain_parts[i-1:])
            else:
                subdomain = text_type(".").join(domain_parts[:i-1])
                domain = text_type(".").join(domain_parts[i-1:i])
                suffix = text_type(".").join(domain_parts[i:])
                return Result(subdomain, domain, suffix)

    if fail_silently:
        return None
    else:
        raise TldDomainNotFound(domain_name=domain_name)
