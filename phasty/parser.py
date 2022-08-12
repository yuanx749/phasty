"""A module parse the output file format of PHAST."""

import configparser
from argparse import Namespace
from ast import literal_eval
from io import StringIO
from typing import List

import numpy as np


def _eval(s: str):
    try:
        return literal_eval(s)
    except (ValueError, SyntaxError):
        return s


def _convert_section(section: configparser.SectionProxy):
    d = {}
    for k, v in section.items():
        if "\n" in v:
            d[k] = np.loadtxt(StringIO(v))
        elif " " in v:
            d[k] = [_eval(e) for e in v.split(" ")]
        else:
            d[k] = _eval(v)
    return Namespace(**d)


def parse_mod(mod_fname: str) -> List[Namespace]:
    """Convert .mod file into dictionaries.

    Args:
        mod_fname: A string of the file name.

    Returns:
        A list of `Namespace` objects represents the data of the input file.
    """
    with open(mod_fname) as f:
        lst = f.readlines()
    for i, row in enumerate(lst):
        if row[0] == "-":
            # add indentation before the first element for configparser
            lst[i] = " " + row
    mod_str = "".join(lst)
    mod_parser = configparser.ConfigParser(delimiters=":")
    mod_lst = []
    n = 0
    for mod in mod_str.split("\n\n"):
        mod_parser.read_string(f"[{n}]\n" + mod)
        mod_lst.append(_convert_section(mod_parser[f"{n}"]))
        n += 1
    return mod_lst


__all__ = [name for name in dir() if not name.startswith("_")]
