from faker import Faker
from constants import URLS_COUNT

__all__ = (
    'URLS',
)


fake = Faker()
fake.seed(URLS_COUNT)


URLS = [fake.url() for _ in range(URLS_COUNT)]
