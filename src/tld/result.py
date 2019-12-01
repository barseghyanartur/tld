__author__ = 'Artur Barseghyan'
__copyright__ = '2013-2019 Artur Barseghyan'
__license__ = 'MPL-1.1 OR GPL-2.0-only OR LGPL-2.0-or-later'
__all__ = (
    'Result',
)


class Result(object):
    """Container."""

    __slots__ = ('subdomain', 'domain', 'tld', '__fld', 'parsed_url')

    def __init__(self, tld: str, domain: str, subdomain: str, parsed_url):
        self.tld = tld
        self.domain = domain if domain != '' else tld
        self.subdomain = subdomain
        self.parsed_url = parsed_url

        if domain:
            self.__fld = f"{self.domain}.{self.tld}"
        else:
            self.__fld = self.tld

    @property
    def extension(self):
        """Alias of ``tld``.

        :return str:
        """
        return self.tld
    suffix = extension

    @property
    def fld(self):
        """First level domain.

        :return:
        :rtype: str
        """
        return self.__fld

    def __str__(self):
        return self.tld
    __repr__ = __str__
    __unicode__ = __str__

    @property
    def __dict__(self):
        """Mimic __dict__ functionality.

        :return:
        :rtype: dict
        """
        return {
            'tld': self.tld,
            'domain': self.domain,
            'subdomain': self.subdomain,
            'fld': self.fld,
            'parsed_url': self.parsed_url,
        }
