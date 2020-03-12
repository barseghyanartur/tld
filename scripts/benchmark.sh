#!/usr/bin/env bash
pycallgraph \
  --stdlib \
  --include "tld.*" \
  --include "urllib.*" \
  --include "codecs.*" \
  --include "functools.*" \
  --include "os.*" \
  --include "sys.*" \
  --include "argparse.*" \
  graphviz \
  -- benchmarks/profile.py
