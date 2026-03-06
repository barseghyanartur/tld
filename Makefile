# Update version ONLY here
VERSION := 0.13.1
SHELL := /bin/bash
# Makefile for project
VENV := ~/.virtualenvs/tld/bin/activate
UNAME_S := $(shell uname -s)

# Build documentation using Sphinx and zip it
build_docs:
	source $(VENV) && python scripts/generate_project_source_tree.py
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

pre-commit-install:
	pre-commit install

pre-commit: pre-commit-install
	pre-commit run --all-files

pyupgrade:
	pre-commit run --all-files pyupgrade

doc8:
	source $(VENV) && doc8

# Run ruff on the codebase
ruff:
	source $(VENV) && ruff check .

# Serve the built docs on port 5001
serve_docs:
	source $(VENV) && cd builddocs && python -m http.server 5001

# Install the project
install:
	source $(VENV) && pip install -e .[all]

# Uninstall the project
uninstall: clean
	source $(VENV) && pip uninstall tld -y

clear-virtualenvs:
	virtualenv --clear tld-py27
	virtualenv --clear tld-py35

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

test: clean
	source $(VENV) && python -m pytest

shell:
	source $(VENV) && ipython

create-secrets:
	source $(VENV) && detect-secrets scan > .secrets.baseline

detect-secrets:
	source $(VENV) && detect-secrets scan --baseline .secrets.baseline

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
	rm src/tld.egg-info -rf
	rm builddocs.zip -rf

compile-requirements:
	source $(VENV) && uv pip compile pyproject.toml requirements/base.in --all-extras -o requirements/base.txt
	source $(VENV) && uv pip compile pyproject.toml requirements/bench.in --all-extras -o requirements/bench.txt
	source $(VENV) && uv pip compile pyproject.toml requirements/build.in --all-extras -o requirements/build.txt
	source $(VENV) && uv pip compile pyproject.toml requirements/code_style.in --all-extras -o requirements/code_style.txt
	source $(VENV) && uv pip compile pyproject.toml requirements/debug.in --all-extras -o requirements/debug.txt
	source $(VENV) && uv pip compile pyproject.toml requirements/dev.in --all-extras -o requirements/dev.txt
	source $(VENV) && uv pip compile pyproject.toml requirements/docs.in --all-extras -o requirements/docs.txt
	source $(VENV) && uv pip compile pyproject.toml requirements/release.in --all-extras -o requirements/release.txt
	source $(VENV) && uv pip compile pyproject.toml requirements/test.in --all-extras -o requirements/test.txt
	source $(VENV) && uv pip compile pyproject.toml requirements/testing.in --all-extras -o requirements/testing.txt

compile-requirements-upgrade:
	source $(VENV) && uv pip compile pyproject.toml requirements/base.in --all-extras -o requirements/base.txt --upgrade
	source $(VENV) && uv pip compile pyproject.toml requirements/bench.in --all-extras -o requirements/bench.txt --upgrade
	source $(VENV) && uv pip compile pyproject.toml requirements/build.in --all-extras -o requirements/build.txt --upgrade
	source $(VENV) && uv pip compile pyproject.toml requirements/code_style.in --all-extras -o requirements/code_style.txt --upgrade
	source $(VENV) && uv pip compile pyproject.toml requirements/debug.in --all-extras -o requirements/debug.txt --upgrade
	source $(VENV) && uv pip compile pyproject.toml requirements/dev.in --all-extras -o requirements/dev.txt --upgrade
	source $(VENV) && uv pip compile pyproject.toml requirements/docs.in --all-extras -o requirements/docs.txt --upgrade
	source $(VENV) && uv pip compile pyproject.toml requirements/release.in --all-extras -o requirements/release.txt --upgrade
	source $(VENV) && uv pip compile pyproject.toml requirements/test.in --all-extras -o requirements/test.txt --upgrade
	source $(VENV) && uv pip compile pyproject.toml requirements/testing.in --all-extras -o requirements/testing.txt --upgrade

update-version:
	@echo "Updating version in pyproject.toml and __init__.py"
	@if [ "$(UNAME_S)" = "Darwin" ]; then \
		gsed -i 's/version = "[0-9.]\+"/version = "$(VERSION)"/' pyproject.toml; \
		gsed -i 's/__version__ = "[0-9.]\+"/__version__ = "$(VERSION)"/' src/pytest_codeblock/__init__.py; \
	else \
		sed -i 's/version = "[0-9.]\+"/version = "$(VERSION)"/' pyproject.toml; \
		sed -i 's/__version__ = "[0-9.]\+"/__version__ = "$(VERSION)"/' src/pytest_codeblock/__init__.py; \
	fi

generate-project-source-tree: clean
	source $(VENV) && python scripts/generate_project_source_tree.py

build:
	source $(VENV) && python -m build .

check-build:
	source $(VENV) && twine check dist/*

release:
	source $(VENV) && twine upload dist/* --verbose

test-release:
	source $(VENV) && twine upload --repository testpypi dist/* --verbose

mypy:
	source $(VENV) && mypy src/tld/

%:
	@:
