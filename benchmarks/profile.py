import os
import sys

from tld import get_tld

path = os.path.join(os.path.abspath(os.path.dirname(__name__)), "benchmarks")

sys.path.insert(0, path)

from constants import TEST_CYCLES, URLS  # noqa

try:
    if callable(profile):  # noqa
        pass
except Exception:
    from fallbacks import profile


@profile
def main():
    for _ in range(TEST_CYCLES):
        for url in URLS:
            get_tld(
                url,
                fix_protocol=True,
                search_public=True,
                search_private=True,
                fail_silently=True,
            )


if __name__ == "__main__":
    main()
