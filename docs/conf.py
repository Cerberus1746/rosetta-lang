"""
Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full
list see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html

Path Setup
==========

If extensions (or modules to document with autodoc) are in another directory,
add these directories to sys.path here. If the directory is relative to the
documentation root, use os.path.abspath to make it absolute, like shown here.
"""
import os
import sys

sys.path.insert(0, os.path.abspath("../src"))

import rosetta_lang


"""
Project Information
===================
"""
project = "rosetta-lang"
copyright = rosetta_lang.__copyright__
author = rosetta_lang.__author__
version = rosetta_lang.__version__


"""
General Configuration
=====================
"""

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx_autodoc_typehints",
]

"""
Add any Sphinx extension module names here, as strings. They can be extensions
coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
"""
autodoc_typehints = "description"

templates_path = ["_templates"]
"""Add any paths that contain templates here, relative to this directory."""


exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
"""
List of patterns, relative to source directory, that match files and
directories to ignore when looking for source files. This pattern also affects
html_static_path and html_extra_path.
"""

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.doctest",
    "sphinx_autodoc_typehints",
]

intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}
html_theme = "nature"
