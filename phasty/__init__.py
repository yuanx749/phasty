"""A Python interface for PHAST."""

__version__ = "0.1.0"

from .wrapper import phylofit
from .parser import parse_mod

__all__ = ["phylofit", "parse_mod"]
