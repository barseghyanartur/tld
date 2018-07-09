#!/usr/bin/env bash

version = ""

if [[ $1 == "--version" ]]
then
    version="$2"
    shift
    shift
    args="$@"
else
    echo "You should provide a --version argument."
fi

if [[ $version ]]
then
    python setup.py sdist bdist_wheel
    py2dsc-deb "dist/tld-$version.tar.gz"
fi
