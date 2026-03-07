Project source-tree
===================

Below is the layout of the project (to 10 levels), followed by
the contents of each key file.

.. code-block:: text
   :caption: Project directory layout

   tld/
   ├── benchmarks
   │   ├── __init__.py
   │   ├── constants.py
   │   ├── factories.py
   │   ├── fallbacks.py
   │   ├── profile.py
   │   └── README.rst
   ├── docs
   │   ├── conf.py
   │   └── tld.rst
   ├── examples
   │   ├── custom_tld_names_source
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
   ├── requirements
   │   ├── bench.in
   │   └── bench.txt
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
   ├── conftest.py
   ├── CONTRIBUTING.rst
   ├── Makefile
   ├── MANIFEST.in
   ├── pyproject.toml
   ├── README.rst
   ├── runtests.py
   ├── setup.cfg
   ├── tox.ini
   └── tox_multi.ini

README.rst
----------

.. literalinclude:: ../README.rst
   :language: rst
   :caption: README.rst

CONTRIBUTING.rst
----------------

.. literalinclude:: ../CONTRIBUTING.rst
   :language: rst
   :caption: CONTRIBUTING.rst

benchmarks/README.rst
---------------------

.. literalinclude:: ../benchmarks/README.rst
   :language: rst
   :caption: benchmarks/README.rst

benchmarks/__init__.py
----------------------

.. literalinclude:: ../benchmarks/__init__.py
   :language: python
   :caption: benchmarks/__init__.py

benchmarks/constants.py
-----------------------

.. literalinclude:: ../benchmarks/constants.py
   :language: python
   :caption: benchmarks/constants.py

benchmarks/factories.py
-----------------------

.. literalinclude:: ../benchmarks/factories.py
   :language: python
   :caption: benchmarks/factories.py

benchmarks/fallbacks.py
-----------------------

.. literalinclude:: ../benchmarks/fallbacks.py
   :language: python
   :caption: benchmarks/fallbacks.py

benchmarks/profile.py
---------------------

.. literalinclude:: ../benchmarks/profile.py
   :language: python
   :caption: benchmarks/profile.py

conftest.py
-----------

.. literalinclude:: ../conftest.py
   :language: python
   :caption: conftest.py

docs/conf.py
------------

.. literalinclude:: conf.py
   :language: python
   :caption: docs/conf.py

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

pyproject.toml
--------------

.. literalinclude:: ../pyproject.toml
   :language: toml
   :caption: pyproject.toml

runtests.py
-----------

.. literalinclude:: ../runtests.py
   :language: python
   :caption: runtests.py

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
