#!/usr/bin/env bash
reset
./scripts/uninstall.sh
./scripts/install.sh
python -m unittest src.tld.tests
