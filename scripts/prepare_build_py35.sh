#!/usr/bin/env bash
./scripts/uninstall.sh
./scripts/clean_up.sh
rm -rf src_py35/
cp -R src/ src_py35/
py-backwards -i src/ -o src_py35/ -t 2.7 -d
sed -i '' -e 's/unicode(/str(/g' $(find src_py35 -type f)
python setup.py sdist bdist_wheel --python-tag py35
rm -rf dist_py35/
mv dist/ dist_py35/

if [[ $1 == "--keep-tar-gz" ]]
then
  shift
else
  rm dist_py35/*.tar.gz
fi
