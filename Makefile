# Update version ONLY here
VERSION := 0.13.2
SHELL := /bin/bash
# Makefile for project
VENV := .venv/bin/activate
UNAME_S := $(shell uname -s)

# ----------------------------------------------------------------------------
# Documentation
# ----------------------------------------------------------------------------

# Build documentation using Sphinx and zip it
build_docs:
	source $(VENV) && sphinx-source-tree
	source $(VENV) && sphinx-build -n -b text docs builddocs
	source $(VENV) && sphinx-build -n -a -b html docs builddocs
	cd builddocs && zip -r ../builddocs.zip . -x ".*" && cd ..

rebuild_docs: clean
	source $(VENV) && sphinx-apidoc . --full -o docs -H 'tld' -A 'Artur Barseghyan <artur.barseghyan@gmail.com>' -f -d 20
	cp docs/conf.py.distrib docs/conf.py
	cp docs/index.rst.distrib docs/index.rst

build_docs_epub:
	$(MAKE) -C docs/ epub

build_docs_pdf:
	$(MAKE) -C docs/ latexpdf

auto_build_docs:
	source $(VENV) && sphinx-autobuild docs docs/_build/html

# Serve the built docs on port 5001
serve_docs:
	source $(VENV) && cd builddocs && python -m http.server 5001

# ----------------------------------------------------------------------------
# Pre-commit
# ----------------------------------------------------------------------------

pre-commit-install:
	pre-commit install

pre-commit: pre-commit-install
	pre-commit run --all-files

# ----------------------------------------------------------------------------
# Linting
# ----------------------------------------------------------------------------

pyupgrade:
	pre-commit run --all-files pyupgrade

doc8:
	source $(VENV) && doc8

# Run ruff on the codebase
ruff:
	source $(VENV) && ruff check .

mypy:
	source $(VENV) && mypy src/tld/

# ----------------------------------------------------------------------------
# Installation
# ----------------------------------------------------------------------------

create-venv:
	uv venv

# Install the project
install: create-venv
	source $(VENV) && uv pip install -e .[all]

# Uninstall the project
uninstall: clean
	source $(VENV) && uv pip uninstall tld -y

# ----------------------------------------------------------------------------
# Tests
# ----------------------------------------------------------------------------

benchmark:
	source $(VENV) && pycallgraph \
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

cprofile:
	source $(VENV) && python -m cProfile -o profile.cprof benchmarks/profile.py
	source $(VENV) && pyprof2calltree -k -i profile.cprof

line-profiler:
	source $(VENV) && kernprof -l -b -v benchmarks/profile.py

# Run core tests
test: clean
	source $(VENV) && pytest -vrx -s

tox:
	source $(VENV) && tox

profile-test:
	source $(VENV) && python -m cProfile -o runtests.cprof runtests.py
	source $(VENV) && pyprof2calltree -k -i runtests.cprof

# ----------------------------------------------------------------------------
# Development
# ----------------------------------------------------------------------------

shell:
	source $(VENV) && ipython

# Clean up generated files
clean:
	find . -type f -name "*.pyc" -exec rm -rf {} \;
	find . -type f -name "__pycache__" -exec rm -rf {} \;
	find . -type d -name "__pycache__" -exec rm -rf {} \; -prune
	find . -type f -name "*.orig" -exec rm -rf {} \;
	find . -type f -name "mprofile_*.dat" -exec rm -rf {} \;
	find . -type f -name "profile.cprof" -exec rm -rf {} \;
	find . -type f -name "profile.py.lprof" -exec rm -rf {} \;
	find . -type f -name "profiler.py.lprof" -exec rm -rf {} \;
	find . -type f -name "pycallgraph*.*" -exec rm -rf {} \;
	find . -type f -name "builddocs.zip" -exec rm -f {} \;
	find . -type f -name "*.py,cover" -exec rm -f {} \;
	find . -type f -name "*.orig" -exec rm -f {} \;
	find . -type f -name "*.coverage" -exec rm -f {} \;
	find . -type f -name "*.db" -exec rm -f {} \;
	rm -rf build/
	rm -rf dist/
	rm -rf .cache/
	rm -rf htmlcov/
	rm -rf builddocs/
	rm -rf testdocs/
	rm -rf .coverage
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf .ruff_cache/
	rm -rf dist/
	rm -rf dist_py27/
	rm -rf dist_py35/
	rm -rf deb_dist/
	rm -rf src/tld.egg-info
	rm -rf builddocs.zip

compile-requirements:
	source $(VENV) && uv pip compile pyproject.toml requirements/bench.in --all-extras -o requirements/bench.txt
	source $(VENV) && uv pip compile pyproject.toml requirements/build.in --all-extras -o requirements/build.txt
	source $(VENV) && uv pip compile pyproject.toml --all-extras -o docs/requirements.txt

compile-requirements-upgrade:
	source $(VENV) && uv pip compile pyproject.toml requirements/bench.in --all-extras -o requirements/bench.txt --upgrade
	source $(VENV) && uv pip compile pyproject.toml requirements/build.in --all-extras -o requirements/build.txt --upgrade
	source $(VENV) && uv pip compile pyproject.toml --all-extras -o docs/requirements.txt --upgrade

# ----------------------------------------------------------------------------
# Security
# ----------------------------------------------------------------------------

create-secrets:
	source $(VENV) && detect-secrets scan > .secrets.baseline

detect-secrets:
	source $(VENV) && detect-secrets scan --baseline .secrets.baseline

# ----------------------------------------------------------------------------
# Release
# ----------------------------------------------------------------------------

update-version:
	@echo "Updating version in pyproject.toml and __init__.py"
	@if [ "$(UNAME_S)" = "Darwin" ]; then \
		gsed -i 's/version = "[0-9.]\+"/version = "$(VERSION)"/' pyproject.toml; \
		gsed -i 's/__version__ = "[0-9.]\+"/__version__ = "$(VERSION)"/' src/tld/__init__.py; \
	else \
		sed -i 's/version = "[0-9.]\+"/version = "$(VERSION)"/' pyproject.toml; \
		sed -i 's/__version__ = "[0-9.]\+"/__version__ = "$(VERSION)"/' src/tld/__init__.py; \
	fi

build:
	source $(VENV) && python -m build .

check-build:
	source $(VENV) && twine check dist/*

release:
	source $(VENV) && twine upload dist/* --verbose

test-release:
	source $(VENV) && twine upload --repository testpypi dist/* --verbose

# make build-deb VERSION=0.13.2
# make build-deb
build-deb:
	@if [ -z "$(VERSION)" ]; then \
		echo "You should provide a VERSION variable."; \
		exit 1; \
	fi
	py2dsc-deb "dist/tld-$(VERSION).tar.gz"

# ----------------------------------------------------------------------------
# Other
# ----------------------------------------------------------------------------

%:
	@:
