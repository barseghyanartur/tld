#!/usr/bin/env bash
find . -name "*.pyc" -exec rm -rf {} \;
find . -name "__pycache__" -exec rm -rf {} \;
find . -name "*.orig" -exec rm -rf {} \;
find . -name "mprofile_*.dat" -exec rm -rf {} \;
find . -name "profile.cprof" -exec rm -rf {} \;
find . -name "profile.py.lprof" -exec rm -rf {} \;
find . -name "profiler.py.lprof" -exec rm -rf {} \;
find . -name "pycallgraph*.*" -exec rm -rf {} \;

rm -rf .mypy_cache/
rm -rf .pytest_cache/
rm -rf .cache/
rm -rf build/
rm -rf builddocs/
rm -rf dist/
rm -rf dist_py27/
rm -rf dist_py35/
rm -rf deb_dist/
rm src/tld.egg-info -rf
rm builddocs.zip -rf
