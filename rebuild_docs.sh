./uninstall.sh
./install.sh
rm docs/*.rst
rm -rf builddocs/
sphinx-apidoc src/tld --full -o docs -H 'tld' -A 'Artur Barseghyan <artur.barseghyan@gmail.com>' -f -d 20
cp docs/conf.py.distrib docs/conf.py
