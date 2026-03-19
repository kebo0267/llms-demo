# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'LLM chatbots demo'
copyright = '2026'
author = 'AI/ML Boot Camp'
release = '1.3.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',  # Support for Markdown files
    'sphinx.ext.autodoc',  # Auto-generate docs from docstrings
    'sphinx.ext.napoleon',  # Support for Google/NumPy style docstrings
    'sphinx.ext.viewcode',  # Add links to source code
]

# MyST parser configuration
myst_enable_extensions = [
    'colon_fence',  # Support for ::: code fences
    'deflist',  # Support for definition lists
    'fieldlist',  # Support for field lists
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'README.md']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_favicon = '_static/favicon.svg'

# Theme options
html_theme_options = {
    'light_css_variables': {
        'color-brand-primary': '#FF7C00',
        'color-brand-content': '#FF7C00',
    },
    'dark_css_variables': {
        'color-brand-primary': '#FF7C00',
        'color-brand-content': '#FF7C00',
    },
}

# Add source file suffix
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
