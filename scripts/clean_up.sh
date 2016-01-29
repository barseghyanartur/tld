find . -name "*.pyc" -exec rm -rf {} \;
rm -rf build/
rm -rf dist/
rm src/tld.egg-info -rf
rm builddocs.zip