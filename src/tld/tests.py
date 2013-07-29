__title__ = 'tld.tests'
__version__ = '0.3'
__build__ = 0x000003
__author__ = 'Artur Barseghyan'

from tld.utils import get_tld

_ = lambda x: x

if __name__ == '__main__':
    # Testing good patterns
    for url in ['http://www.google.co.uk', 'http://www.v2.google.co.uk', 'http://www.me.congresodelalengua3.ar']:
        print '******** Testing the URL: %s' % url
        print get_tld(url)

    # Testing the bad patterns
    for url in ['/index.php?a=1&b=2', 'v2.www.google.com', 'http://www.tld.doesnotexist']:
        print '******** Testing the URL: %s' % url
        try:
            print get_tld(url)
        except Exception, e:
            print e
