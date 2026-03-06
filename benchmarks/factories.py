from constants import URLS_COUNT
from fake import FAKER

__all__ = ("URLS",)

URLS = [FAKER.url() for _ in range(URLS_COUNT)]
