#!/usr/bin/env bash
./scripts/prepare_build_py35.sh
twine upload dist_py35/*
