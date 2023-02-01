from constants import URLS_COUNT
from faker import Faker

__all__ = ("URLS",)


fake = Faker()
fake.seed(URLS_COUNT)


URLS = [fake.url() for _ in range(URLS_COUNT)]
