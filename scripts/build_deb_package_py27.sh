#!/usr/bin/env bash

version=""

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
    ./scripts/prepare_build_py27.sh --keep-tar-gz
    py2dsc-deb "dist_py27/tld-$version.tar.gz"
fi
