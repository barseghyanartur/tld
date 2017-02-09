from .conf import get_setting

__title__ = 'tld.exceptions'
__author__ = 'Artur Barseghyan'
__copyright__ = '2013-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'TldIOError',
    'TldDomainNotFound',
    'TldBadUrl'
)


class TldIOError(IOError):
    """TldIOError.

    Supposed to be thrown when problems with reading/writing occur."""
    def __init__(self, msg=None):
        TLD_NAMES_LOCAL_PATH = get_setting('NAMES_LOCAL_PATH')
        if msg is None:
            msg = "Can't read from or write to the %s " \
                  "file!" % TLD_NAMES_LOCAL_PATH
        super(TldIOError, self).__init__(msg)


class TldDomainNotFound(ValueError):
    """TldDomainNotFound.

    Supposed to be thrown when domain name is not found (didn't match) the
    local TLD policy.
    """
    def __init__(self, domain_name):
        super(TldDomainNotFound, self).__init__(
            "Domain %s didn't match any existing TLD name!" % domain_name
        )


class TldBadUrl(ValueError):
    """TldBadUrl.

    Supposed to be thrown when bad URL is given.
    """
    def __init__(self, url):
        super(TldBadUrl, self).__init__("Is not a valid URL %s!" % url)
