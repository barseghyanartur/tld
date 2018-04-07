#!/usr/bin/env bash
reset
./scripts/uninstall.sh
./scripts/install.sh
python src/tld/tests.py
