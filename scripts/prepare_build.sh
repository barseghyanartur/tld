#!/usr/bin/env bash
./scripts/uninstall.sh
./scripts/clean_up.sh
python setup.py sdist bdist_wheel --universal
