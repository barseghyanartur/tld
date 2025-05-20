Project source-tree
===================

Below is the layout of our project (to 10 levels), followed by
the contents of each key file.

.. code-block:: bash
   :caption: Project directory layout

   tld/

   ├── docs
   │   ├── _build
   │   ├── _static
   │   ├── _templates
   │   ├── changelog.rst
   │   ├── code_of_conduct.rst
   │   ├── conf.py
   │   ├── conf.py.distrib
   │   ├── contributor_guidelines.rst
   │   ├── documentation.rst
   │   ├── index.rst
   │   ├── index.rst.distrib
   │   ├── llms.rst
   │   ├── make.bat
   │   ├── Makefile
   │   ├── security.rst
   │   ├── source_tree.rst
   │   └── tld.rst
   ├── examples
   │   ├── custom_tld_names_source
   │   │   ├── res
   │   │   │   └── effective_tld_names_custom.dat.txt
   │   │   ├── __init__.py
   │   │   ├── example.py
   │   │   └── parser.py
   │   ├── gae
   │   │   ├── __init__.py
   │   │   ├── data.py
   │   │   ├── example.py
   │   │   └── parser.py
   │   ├── __init__.py
   │   └── README.rst
   ├── scripts
   │   ├── benchmark.sh
   │   ├── build_deb_package.sh
   │   ├── clear_virtualenvs.sh
   │   ├── compile_requirements.sh
   │   ├── cprofile.sh
   │   ├── detect-secrets-create-baseline.sh
   │   ├── doc8.sh
   │   ├── generate_project_source_tree.py
   │   ├── install.sh
   │   ├── isort.sh
   │   ├── line_profiler.sh
   │   ├── make_release.sh
   │   ├── mypy.sh
   │   ├── pycodestyle.sh
   │   ├── pylint.sh
   │   ├── reinstall.sh
   │   ├── ruff.sh
   │   ├── runtests.sh
   │   ├── source_install.sh
   │   ├── test.sh
   │   ├── test_release.sh
   │   ├── uninstall.sh
   │   └── upgrade_requirements.sh
   ├── src
   │   └── tld
   │       ├── res
   │       │   ├── effective_tld_names.dat.txt
   │       │   └── effective_tld_names_public_only.dat.txt
   │       ├── tests
   │       │   ├── res
   │       │   │   └── effective_tld_names_custom.dat.txt
   │       │   ├── __init__.py
   │       │   ├── base.py
   │       │   ├── test_commands.py
   │       │   ├── test_core.py
   │       │   └── test_registry.py
   │       ├── __init__.py
   │       ├── base.py
   │       ├── conf.py
   │       ├── defaults.py
   │       ├── exceptions.py
   │       ├── helpers.py
   │       ├── py.typed
   │       ├── registry.py
   │       ├── result.py
   │       ├── trie.py
   │       └── utils.py

docs/changelog.rst
------------------

.. literalinclude:: changelog.rst
   :language: rst
   :caption: docs/changelog.rst

docs/code_of_conduct.rst
------------------------

.. literalinclude:: code_of_conduct.rst
   :language: rst
   :caption: docs/code_of_conduct.rst

docs/conf.py
------------

.. literalinclude:: conf.py
   :language: python
   :caption: docs/conf.py

docs/contributor_guidelines.rst
-------------------------------

.. literalinclude:: contributor_guidelines.rst
   :language: rst
   :caption: docs/contributor_guidelines.rst

docs/documentation.rst
----------------------

.. literalinclude:: documentation.rst
   :language: rst
   :caption: docs/documentation.rst

docs/index.rst
--------------

.. literalinclude:: index.rst
   :language: rst
   :caption: docs/index.rst

docs/llms.rst
-------------

.. literalinclude:: llms.rst
   :language: rst
   :caption: docs/llms.rst

docs/security.rst
-----------------

.. literalinclude:: security.rst
   :language: rst
   :caption: docs/security.rst

docs/source_tree.rst
--------------------

.. literalinclude:: source_tree.rst
   :language: rst
   :caption: docs/source_tree.rst

docs/tld.rst
------------

.. literalinclude:: tld.rst
   :language: rst
   :caption: docs/tld.rst

examples/README.rst
-------------------

.. literalinclude:: ../examples/README.rst
   :language: rst
   :caption: examples/README.rst

examples/__init__.py
--------------------

.. literalinclude:: ../examples/__init__.py
   :language: python
   :caption: examples/__init__.py

examples/custom_tld_names_source/__init__.py
--------------------------------------------

.. literalinclude:: ../examples/custom_tld_names_source/__init__.py
   :language: python
   :caption: examples/custom_tld_names_source/__init__.py

examples/custom_tld_names_source/example.py
-------------------------------------------

.. literalinclude:: ../examples/custom_tld_names_source/example.py
   :language: python
   :caption: examples/custom_tld_names_source/example.py

examples/custom_tld_names_source/parser.py
------------------------------------------

.. literalinclude:: ../examples/custom_tld_names_source/parser.py
   :language: python
   :caption: examples/custom_tld_names_source/parser.py

examples/gae/__init__.py
------------------------

.. literalinclude:: ../examples/gae/__init__.py
   :language: python
   :caption: examples/gae/__init__.py

examples/gae/data.py
--------------------

.. literalinclude:: ../examples/gae/data.py
   :language: python
   :caption: examples/gae/data.py

examples/gae/example.py
-----------------------

.. literalinclude:: ../examples/gae/example.py
   :language: python
   :caption: examples/gae/example.py

examples/gae/parser.py
----------------------

.. literalinclude:: ../examples/gae/parser.py
   :language: python
   :caption: examples/gae/parser.py

scripts/generate_project_source_tree.py
---------------------------------------

.. literalinclude:: ../scripts/generate_project_source_tree.py
   :language: python
   :caption: scripts/generate_project_source_tree.py

src/tld/__init__.py
-------------------

.. literalinclude:: ../src/tld/__init__.py
   :language: python
   :caption: src/tld/__init__.py

src/tld/base.py
---------------

.. literalinclude:: ../src/tld/base.py
   :language: python
   :caption: src/tld/base.py

src/tld/conf.py
---------------

.. literalinclude:: ../src/tld/conf.py
   :language: python
   :caption: src/tld/conf.py

src/tld/defaults.py
-------------------

.. literalinclude:: ../src/tld/defaults.py
   :language: python
   :caption: src/tld/defaults.py

src/tld/exceptions.py
---------------------

.. literalinclude:: ../src/tld/exceptions.py
   :language: python
   :caption: src/tld/exceptions.py

src/tld/helpers.py
------------------

.. literalinclude:: ../src/tld/helpers.py
   :language: python
   :caption: src/tld/helpers.py

src/tld/registry.py
-------------------

.. literalinclude:: ../src/tld/registry.py
   :language: python
   :caption: src/tld/registry.py

src/tld/result.py
-----------------

.. literalinclude:: ../src/tld/result.py
   :language: python
   :caption: src/tld/result.py

src/tld/tests/__init__.py
-------------------------

.. literalinclude:: ../src/tld/tests/__init__.py
   :language: python
   :caption: src/tld/tests/__init__.py

src/tld/tests/base.py
---------------------

.. literalinclude:: ../src/tld/tests/base.py
   :language: python
   :caption: src/tld/tests/base.py

src/tld/tests/test_commands.py
------------------------------

.. literalinclude:: ../src/tld/tests/test_commands.py
   :language: python
   :caption: src/tld/tests/test_commands.py

src/tld/tests/test_core.py
--------------------------

.. literalinclude:: ../src/tld/tests/test_core.py
   :language: python
   :caption: src/tld/tests/test_core.py

src/tld/tests/test_registry.py
------------------------------

.. literalinclude:: ../src/tld/tests/test_registry.py
   :language: python
   :caption: src/tld/tests/test_registry.py

src/tld/trie.py
---------------

.. literalinclude:: ../src/tld/trie.py
   :language: python
   :caption: src/tld/trie.py

src/tld/utils.py
----------------

.. literalinclude:: ../src/tld/utils.py
   :language: python
   :caption: src/tld/utils.py
