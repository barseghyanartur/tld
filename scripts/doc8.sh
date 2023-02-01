#!/usr/bin/env bash
# Since doc8 seems to ignore settings, we have to check things manually.
# Once that is fixed, switch back to a single `doc8` call.
doc8 *.rst
doc8 *.md
doc8 *.txt
doc8 docs/
doc8 benchmarks/*.rst
doc8 examples/*.rst
doc8 jupyter/*.rst
