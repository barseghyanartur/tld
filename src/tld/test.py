# -*- coding: utf-8 -*-

import logging

__title__ = 'tld.tests'
__author__ = 'Artur Barseghyan'
__copyright__ = '2013-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('TldTest',)

import unittest

from . import defaults
from .conf import get_setting, set_setting
from .utils import get_tld, update_tld_names

LOG_INFO = True
TRACK_TIME = False
LOGGER = logging.getLogger(__name__)


def log_info(func):
    """Log some useful info."""
    if not LOG_INFO:
        return func

    def inner(self, *args, **kwargs):
        """Inner."""
        if TRACK_TIME:
            import simple_timer
            timer = simple_timer.Timer()  # Start timer

        result = func(self, *args, **kwargs)

        if TRACK_TIME:
            timer.stop()  # Stop timer

        LOGGER.debug('\n\n%s', func.__name__)
        LOGGER.debug('============================')
        if func.__doc__:
            LOGGER.debug('""" %s """', func.__doc__.strip())
        LOGGER.debug('----------------------------')
        if result is not None:
            LOGGER.debug(result)
        if TRACK_TIME:
            LOGGER.debug('done in %s seconds', timer.duration)
        LOGGER.debug('\n++++++++++++++++++++++++++++')

        return result
    return inner


class TldTest(unittest.TestCase):
    """Tld tests."""

    def setUp(self):
        """Set up."""
        self.good_patterns = [
            {
                'url': 'http://www.google.co.uk',
                'tld': 'google.co.uk',
                'subdomain': 'www',
                'domain': 'google',
                'suffix': 'co.uk',
            },
            {
                'url': 'http://www.v2.google.co.uk',
                'tld': 'google.co.uk',
                'subdomain': 'www.v2',
                'domain': 'google',
                'suffix': 'co.uk',
            },
            # No longer valid
            # {
            #    'url': 'http://www.me.congresodelalengua3.ar',
            #    'tld': 'me.congresodelalengua3.ar',
            #    'subdomain': 'www',
            #    'domain': 'me',
            #    'suffix': 'congresodelalengua3.ar',
            # },
            {
                'url': u'http://хром.гугл.рф',
                'tld': u'гугл.рф',
                'subdomain': u'хром',
                'domain': u'гугл',
                'suffix': u'рф',
            },
            {
                'url': 'http://www.google.co.uk:8001/lorem-ipsum/',
                'tld': 'google.co.uk',
                'subdomain': 'www',
                'domain': 'google',
                'suffix': 'co.uk',
            },
            {
                'url': 'http://www.me.cloudfront.net',
                'tld': 'me.cloudfront.net',
                'subdomain': 'www',
                'domain': 'me',
                'suffix': 'cloudfront.net',
            },
            {
                'url': 'http://www.v2.forum.tech.google.co.uk:8001/'
                       'lorem-ipsum/',
                'tld': 'google.co.uk',
                'subdomain': 'www.v2.forum.tech',
                'domain': 'google',
                'suffix': 'co.uk',
            },
            {
                'url': 'https://pantheon.io/',
                'tld': 'pantheon.io',
                'subdomain': '',
                'domain': 'pantheon',
                'suffix': 'io',
            }
        ]

        self.bad_patterns = [
            '/index.php?a=1&b=2',
            'v2.www.google.com',
            'http://www.tld.doesnotexist'
        ]

    @log_info
    def test_0_tld_names_loaded(self):
        """Test if tld names are loaded."""
        get_tld('http://www.google.co.uk')
        from .utils import tld_names
        res = len(tld_names) > 0
        self.assertTrue(res)
        return res

    @log_info
    def test_1_update_tld_names(self):
        """Test updating the tld names (re-fetch mozilla source)."""
        res = update_tld_names(fail_silently=True)
        self.assertTrue(res)
        return res

    @log_info
    def test_2_good_patterns_pass(self):
        """Test good URL patterns."""
        res = []
        for data in self.good_patterns:
            _res = get_tld(data['url'], fail_silently=True)
            self.assertEqual(_res, data['tld'])
            res.append(_res)
        return res

    @log_info
    def test_3_bad_patterns_pass(self):
        """Test bad URL patterns."""
        res = []
        for url in self.bad_patterns:
            _res = get_tld(url, fail_silently=True)
            self.assertEqual(_res, None)
            res.append(_res)
        return res

    @log_info
    def test_4_override_settings(self):
        """Testing settings override."""
        def override_settings():
            """Override settings."""
            return get_setting('DEBUG')

        self.assertEqual(defaults.DEBUG, override_settings())

        set_setting('DEBUG', True)

        self.assertEqual(True, override_settings())

        return override_settings()

    @log_info
    def test_5_good_patterns_pass_parsed_object(self):
        """Test good URL patterns."""
        res = []
        for data in self.good_patterns:
            _res = get_tld(data['url'], fail_silently=True, as_object=True)
            self.assertEqual(_res.tld, data['tld'])
            self.assertEqual(_res.subdomain, data['subdomain'])
            self.assertEqual(_res.domain, data['domain'])
            self.assertEqual(_res.suffix, data['suffix'])
            res.append(_res)
        return res


if __name__ == '__main__':
    unittest.main()
