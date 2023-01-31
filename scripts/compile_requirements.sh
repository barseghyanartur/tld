#!/usr/bin/env bash
cd requirements/

echo "base.in"
pip-compile base.in "$@"

echo "bench.in"
pip-compile bench.in "$@"

echo "build.in"
pip-compile build.in "$@"

echo "code_style.in"
pip-compile code_style.in "$@"

echo "debug.in"
pip-compile debug.in "$@"

echo "dev.in"
pip-compile dev.in "$@"

echo "docs.in"
pip-compile docs.in "$@"

echo "release.in"
pip-compile release.in "$@"

echo "test.in"
pip-compile test.in "$@"

echo "testing.in"
pip-compile testing.in "$@"
