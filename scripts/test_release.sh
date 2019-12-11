#!/usr/bin/env bash
./scripts/prepare_build.sh
python setup.py register
twine upload --repository-url https://test.pypi.org/legacy/ dist/* dist_py35/*
