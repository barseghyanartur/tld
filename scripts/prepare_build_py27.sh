#!/usr/bin/env bash
./scripts/uninstall.sh
./scripts/clean_up.sh
rm -rf src_py27/
cp -R src/ src_py27/
py-backwards -i src/ -o src_py27/ -t 2.7 -d
cp -R src/tld/res/ src_py27/tld/
sed -i '' -e 's/from functools import lru_cache/from backports.functools_lru_cache import lru_cache/g' $(find src_py27 -type f)
sed -i '' -e "s/= type(u'/= type('/g" $(find src_py27 -type f)
sed -i '' -e "s/=u'/='/g" $(find src_py27 -type f)
sed -i '' -e "s/u'uid/'uid/g" $(find src_py27 -type f)
sed -i '' -e "s/u'source/'source/g" $(find src_py27 -type f)
sed -i '' -e "s/u'local/'local/g" $(find src_py27 -type f)
sed -i '1i# -*- coding: utf-8 -*-' src_py27/tld/*.py
sed -i '1i# -*- coding: utf-8 -*-' src_py27/tld/tests/*.py
sed -i '' -e "s/from __future__ import unicode_literals//g" src_py27/tld/tests/test_core.py
sed -i '' -e "s/with self.subTest(.*):/if True:/g" $(find src_py27 -type f)

python setup.py sdist bdist_wheel --python-tag py27
rm -rf dist_py27/
mv dist/ dist_py27/
rm dist_py27/*.tar.gz
