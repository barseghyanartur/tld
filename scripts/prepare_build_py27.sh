#!/usr/bin/env bash
./scripts/uninstall.sh
./scripts/clean_up.sh
rm -rf src_py27/
cp -R src/ src_py27/
py-backwards -i src/ -o src_py27/ -t 2.7 -d
#sed -i '' -e 's/unicode(/str(/g' $(find src_py35 -type f)
python setup.py sdist bdist_wheel --python-tag py27
rm -rf dist_py27/
mv dist/ dist_py27/
rm dist_py27/*.tar.gz
