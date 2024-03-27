# -- Project information -----------------------------------------------------

import os
import sys

project = 'Tech Blog'
copyright = '2024, Roie Black'
author = 'Roie Black'
release = '0.1.0'

# -- General configuration ---------------------------------------------------

sys.path.insert(0, os.path.abspath('.'))

extensions = [
    'sphinx_exts.wordcount',
    'sphinxcontrib.tikz',
    'sphinxcontrib.bibtex',
    'sphinxcontrib.spelling',
    'sphinxcontrib.programoutput',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

bibtex_bibfiles = ['references.bib']

spelling_word_list_filename = ['spelling_wordlist.txt']
spelling_verbose = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'python_docs_theme'
html_static_path = ['_static']
