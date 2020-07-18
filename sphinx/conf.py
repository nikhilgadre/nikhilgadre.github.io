# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Nikhil Gadre'
copyright = '2020, Nikhil Gadre'
author = 'Nikhil Gadre'

# The full version, including alpha/beta/rc tags
release = '2.0.0'


# -- General configuration ---------------------------------------------------
from datetime import datetime
import sphinx_fontawesome
year = datetime.now().year
copyright = u"%d Nikhil Gadre" % year

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]
extensions = ['sphinx_fontawesome']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_title = 'Nikhil Gadre'
html_theme = 'alabaster'

html_sidebars = {
    '**': [
        'about.html',
        'logo.html',
        #'connect.html',
        'navigation.html',
        #'relations.html',
        #'searchbox.html',
        #'donate.html',
    ]
}

html_theme_options = {'nosidebar': False, "description": "Network Engineer | DevOps",
    #"github_user": "bitprophet",
    #"github_repo": "alabaster",
    #"fixed_sidebar": True,
    #"tidelift_url": "https://tidelift.com/subscription/pkg/pypi-alabaster?utm_source=pypi-alabaster&utm_medium=referral&utm_campaign=docs",  # noqa
    }

html_css_files = ["https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']