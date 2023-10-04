# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'The Sappoteers'
copyright = '2023, The Sappoteers'
author = 'Ankit Bhandekar'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

source_dir = 'source'

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

import pydata_sphinx_theme

html_theme = "pydata_sphinx_theme"
html_static_path = ['_static']
html_css_files = [
    "custom.css",
]
html_title = "THE SAPPOTEERS"
html_logo = '_static/logo.png'
html_baseurl = 'https://sappoteers.github.io/'
html_show_sourcelink = False
html_theme_options = {
    "logo": {
        "text": "THE SAPPOTEERS",
        "image_dark": "_static/logo.png",  # assuming your logo file is named logo.png and located in the _static directory
        "alt_text": "THE SAPPOTEERS",
    },
    "footer_end": ["combined_footer.html"],
}

def setup(app):
    app.add_css_file('custom.css')
