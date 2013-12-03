from __future__ import print_function

__title__ = 'tld.tests'
__author__ = 'Artur Barseghyan'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('TldTest',)

import unittest

from tld.utils import get_tld, update_tld_names
from tld.conf import get_setting, set_setting
from tld import defaults

_ = lambda x: x

PRINT_INFO = True
TRACK_TIME = False

def print_info(func):
    """
    Prints some useful info.
    """
    if not PRINT_INFO:
        return func

    def inner(self, *args, **kwargs):
        if TRACK_TIME:
            import simple_timer
            timer = simple_timer.Timer() # Start timer

        result = func(self, *args, **kwargs)

        if TRACK_TIME:
            timer.stop() # Stop timer

        print('\n\n%s' % func.__name__)
        print('============================')
        if func.__doc__:
            print('""" %s """' % func.__doc__.strip())
        print('----------------------------')
        if result is not None:
            print(result)
        if TRACK_TIME:
            print('done in %s seconds' % timer.duration)
        print('\n++++++++++++++++++++++++++++')

        return result
    return inner

class TldTest(unittest.TestCase):
    """
    Tld tests.
    """
    def setUp(self):
        self.good_patterns = [
            'http://www.google.co.uk',
            'http://www.v2.google.co.uk',
            'http://www.me.congresodelalengua3.ar',
            'http://www.google.co.uk:8001/lorem-ipsum/',
        ]

        self.bad_patterns = [
            '/index.php?a=1&b=2',
            'v2.www.google.com',
            'http://www.tld.doesnotexist'
        ]

    @print_info
    def test_0_tld_names_loaded(self):
        """
        Test if tld names are loaded.
        """
        get_tld('http://www.google.co.uk')
        from tld.utils import tld_names
        res = len(tld_names) > 0
        self.assertTrue(res)
        return res

    @print_info
    def test_1_update_tld_names(self):
        """
        Test updating the tld names (re-fetch mozilla source).
        """
        res = update_tld_names(fail_silently=True)
        self.assertTrue(res)
        return res

    @print_info
    def test_2_good_patterns_pass(self):
        """
        Test good URL patterns.
        """
        res = []
        for url in self.good_patterns:
            r = get_tld(url, fail_silently=True)
            self.assertNotEqual(r, None)
            res.append(r)
        return res

    @print_info
    def test_3_bad_patterns_pass(self):
        """
        Test bad URL patterns.
        """
        res = []
        for url in self.bad_patterns:
            r = get_tld(url, fail_silently=True)
            self.assertEqual(r, None)
            res.append(r)
        return res

    @print_info
    def test_4_override_settings(self):
        """
        Testing settings override.
        """
        def override_settings():
            return get_setting('DEBUG')

        self.assertEqual(defaults.DEBUG, override_settings())

        set_setting('DEBUG', True)

        self.assertEqual(True, override_settings())

        return override_settings()

if __name__ == '__main__':
    unittest.main()

