#!/usr/bin/env bash
cd requirements/
pip-compile base.in --upgrade
pip-compile bench.in --upgrade
pip-compile build.in --upgrade
pip-compile code_style.in --upgrade
pip-compile debug.in --upgrade
pip-compile docs.in --upgrade
pip-compile release.in --upgrade
pip-compile test.in --upgrade
pip-compile testing.in --upgrade
