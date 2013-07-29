__title__ = 'tld.exceptions'
__version__ = '0.3'
__build__ = 0x000003
__author__ = 'Artur Barseghyan'
__all__ = ('TldIOError', 'TldDomainNotFound', 'TldBadUrl')

from tld.settings import NAMES_LOCAL_PATH as TLD_NAMES_LOCAL_PATH

_ = lambda x: x

class TldIOError(IOError):
    """
    Supposed to be thrown when problems with reading/writing occur.
    """
    def __init__(self, msg=None):
        if msg is None:
            msg = _("Can't read from or write to the %s file!") % TLD_NAMES_LOCAL_PATH
        super(TldIOError, self).__init__(msg)

class TldDomainNotFound(ValueError):
    """
    Supposed to be thrown when domain name is not found (didn't match) the local TLD policy.
    """
    def __init__(self, domain_name):
        super(TldDomainNotFound, self).__init__(_("Domain %s didn't match any existing TLD name!") % domain_name)

class TldBadUrl(ValueError):
    """
    Supposed to be thrown when bad URL is given.
    """
    def __init__(self, url):
        super(TldBadUrl, self).__init__(_("Is not a valid URL %s!") % url)
