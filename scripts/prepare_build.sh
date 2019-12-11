#!/usr/bin/env bash
./scripts/uninstall.sh
./scripts/clean_up.sh
python setup.py sdist bdist_wheel --python-tag py36
python setup.py sdist bdist_wheel --python-tag py37
python setup.py sdist bdist_wheel --python-tag py38
