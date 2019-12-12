#!/usr/bin/env bash
./scripts/prepare_build_py27.sh
twine upload dist_py27/*
