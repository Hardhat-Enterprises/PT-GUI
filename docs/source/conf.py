# Configuration file for the Sphinx documentation builder.

# -- Project information

# pylint: disable=redefined-builtin
# pylint: disable=invalid-name
# pylint: disable=missing-module-docstring

project = 'Deakin Detonator Toolkit'
copyright = '2022, Deakin'
author = 'Deakin University'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
