#!/usr/bin/env bash
python -m cProfile -o profile.cprof benchmarks/profile.py
pyprof2calltree -k -i profile.cprof
