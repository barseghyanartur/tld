#!/usr/bin/env bash
./scripts/clean_up.sh
sphinx-apidoc src/tld src/tld/tests/* --full -o docs -H 'tld' -A 'Artur Barseghyan <artur.barseghyan@gmail.com>' -f -d 20
cp docs/conf.py.distrib docs/conf.py
cp docs/index.rst.distrib docs/index.rst
