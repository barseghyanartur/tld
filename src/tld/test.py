__title__ = 'tld.tests'
__version__ = '0.4'
__build__ = 0x000004
__author__ = 'Artur Barseghyan'
__all__ = ('TldTest',)

import unittest

from tld.utils import get_tld, update_tld_names
from tld.conf import get_setting, set_setting
from tld import defaults

_ = lambda x: x

TRACK_TIME = True

def track_time(func):
    """
    Prints some useful info.
    """
    if not TRACK_TIME:
        return func

    def inner(self, *args, **kwargs):
        #timer = simple_timer.Timer() # Start timer

        result = func(self, *args, **kwargs)

        #timer.stop() # Stop timer

        print '\n%s' % func.__name__
        print '============================'
        print '""" %s """' % func.__doc__.strip()
        print '----------------------------'
        if result is not None: print result
        #print 'done in %s seconds' % timer.duration

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
            'http://www.me.congresodelalengua3.ar'
        ]

        self.bad_patterns = [
            '/index.php?a=1&b=2',
            'v2.www.google.com',
            'http://www.tld.doesnotexist'
        ]

    @track_time
    def test_0_tld_names_loaded(self):
        """
        Test if tld names are loaded.
        """
        get_tld('http://www.google.co.uk')
        from tld.utils import tld_names
        res = len(tld_names) > 0
        self.assertEqual(res, True)
        return res

    @track_time
    def test_1_update_tld_names(self):
        """
        Test updating the tld names (re-fetch mozilla source).
        """
        res = update_tld_names(fail_silently=True)
        self.assertEqual(res, True)
        return res

    @track_time
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

    @track_time
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

    @track_time
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
