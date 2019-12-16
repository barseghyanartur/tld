#!/usr/bin/env python
import os
import sys
import pytest

py_package_dir = 'src'

try:
    if sys.argv[-2] == '--python-tag':
        if sys.argv[-1] == 'py35':
            py_package_dir = 'src_py35'
        elif sys.argv[-1] == 'py27':
            py_package_dir = 'src_py35'
        sys.argv.pop(-1)
        sys.argv.pop(-1)
except Exception as err:
    pass

sys.argv.append(py_package_dir)


def main():
    sys.path.insert(0, os.path.abspath(py_package_dir))
    return pytest.main()


if __name__ == '__main__':
    try:
        main = profile(main)
        sys.exit(main())
    except Exception:
        sys.exit(main())
