#!/usr/bin/env bash
reset
pycodestyle src/tld/ --exclude src/tld/sources/,src/tld/base.py
