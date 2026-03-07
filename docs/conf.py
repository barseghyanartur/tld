# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath(os.path.join("..", "src")))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

try:
    import tld

    version = tld.__version__
    project = tld.__title__
    copyright = tld.__copyright__
    author = tld.__author__
except Exception:
    version = "0.1"
    project = "tld"
    copyright = "2013-2026, Artur Barseghyan <artur.barseghyan@gmail.com>"
    author = "Artur Barseghyan <artur.barseghyan@gmail.com>"

author_name = "Artur Barseghyan"
author_email = "artur.barseghyan@gmail.com"
doc_title = "tld Documentation"
description = "Extract the top level domain (TLD) from the URL given."

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc", 
    "sphinx.ext.viewcode",
    "sphinx.ext.todo",
    "sphinx_no_pragma",
    "sphinx_llms_txt_link",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "en"

release = version

# The suffix of source filenames.
source_suffix = {
    ".rst": "restructuredtext",
}

pygments_style = "sphinx"

# The master toctree document.
master_doc = "index"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# -- Options for todo extension ----------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/todo.html#configuration

todo_include_todos = True

# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',
}

latex_documents = [
    (
        "index",
        "tld.tex",
        doc_title,
        "Artur Barseghyan \\textless{}"
        "artur.barseghyan@gmail.com\\textgreater{}",
        "manual",
    ),
]

# -- Options for manual page output --------------------------------------------

man_pages = [
    (
        "index",
        project,
        doc_title,
        [author],
        1,
    )
]

# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        "index",
        project,
        doc_title,
        author,
        project,
        description,
        "Miscellaneous",
    ),
]

# -- Options for Epub output  ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = "GitHub"
epub_copyright = copyright
epub_identifier = "https://github.com/barseghyanartur/tld"  # URL or ISBN
epub_scheme = "URL"  # or "ISBN"
epub_uid = "https://github.com/barseghyanartur/tld"
