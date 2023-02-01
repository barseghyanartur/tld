#!/usr/bin/env python
import os
import sys

import pytest

py_package_dir = "src"

try:
    if os.environ.get("PYTHON_TAG") == "py35":
        py_package_dir = "src_py35"
    elif os.environ.get("PYTHON_TAG") == "py27":
        py_package_dir = "src_py27"
except Exception:
    pass

# sys.argv.append(py_package_dir)

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
    sys.path.insert(0, os.path.abspath(py_package_dir))
    return pytest.main()


if __name__ == "__main__":
    sys.exit(main())
