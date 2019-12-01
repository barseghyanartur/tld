# from timeit import default_timer as timer
# from faker import Faker
from tld import get_tld


# fake = Faker()
# fake.seed(1234)

URLS_COUNT = 1000
# URLS = [fake.url() for _ in range(URLS_COUNT)]
URLS = [
    'http://www.google.co.uk',
    'http://www.v2.google.co.uk',
    'http://www.google.co.uk:8001/lorem-ipsum/',
    'http://www.me.cloudfront.net',
    'http://www.v2.forum.tech.google.co.uk:8001/lorem-ipsum/',
    'https://pantheon.io/',
]
TIMES = 100

# start = timer()
for _ in range(TIMES):
    for url in URLS:
        tld = get_tld(url)

# print('get_tld:', timer() - start)
