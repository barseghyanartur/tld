#!/usr/bin/env python
import os
import sys

import pytest

py_package_dir = "src"

try:
    profile  # noqa
except Exception:
    from functools import wraps

    def profile(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapped


@profile
def main():
    sys.path.insert(0, os.path.abspath("src"))
    return pytest.main()


if __name__ == "__main__":
    sys.exit(main())
