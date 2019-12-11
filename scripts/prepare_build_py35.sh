#!/usr/bin/env bash
./scripts/uninstall.sh
./scripts/clean_up.sh
cp -R src/ src_py35/
python setup.py sdist bdist_wheel --python-tag py35
rm -rf dist_py35/
mv dist/ dist_py35/
rm dist_py35/*.tar.gz
