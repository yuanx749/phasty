import os
import sys

sys.path.insert(0, os.path.abspath(".."))

project = "phasty"
copyright = "2022, yuanx749"
author = "yuanx749"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "myst_parser",
    "sphinx_copybutton",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "furo"

autodoc_mock_imports = ["numpy"]

autosummary_ignore_module_all = False  # use the order in __all__
