#!/usr/bin/env bash
./scripts/uninstall.sh
./scripts/clean_up.sh
python setup.py sdist bdist_wheel --python-tag py36
python setup.py sdist bdist_wheel --python-tag py37
python setup.py sdist bdist_wheel --python-tag py38
python setup.py sdist bdist_wheel --python-tag py39
python setup.py sdist bdist_wheel --python-tag py310
python setup.py sdist bdist_wheel --python-tag py311
