[![PyPI version](https://badge.fury.io/py/phasty.svg)](https://badge.fury.io/py/phasty)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/yuanx749/phasty.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/yuanx749/phasty/context:python)
[![codecov](https://codecov.io/gh/yuanx749/phasty/branch/main/graph/badge.svg?token=NT7LUW1ECF)](https://codecov.io/gh/yuanx749/phasty)

# phasty
A Python interface for PHAST (phylogenetic analysis with space/time models).

## Description
[PHAST](http://compgen.cshl.edu/phast/) is a package consisting of command-line programs for comparative genomics. It supports several nucleotide substitution models. This package phasty provides Python wrappers for some major programs so that it is easier to integrate them into complicated workflows. It can also parse some files from plain text to more computer-friendly forms to help downstream analysis.

## Usage
The design idea of phasty is to be robust and compatible with version changes of PHAST. Therefore, the signatures of functions are written in a general way. Please refer to the corresponding websites for detailed usage of specific options.

### Example
Assume `hmrc.fa` exists in the current directory. After running `phylo_fit` and reading the .mod file, the content is stored in a list of objects holding attributes with proper data types. Each object represents a fitted model.
```Python
from phasty import phylo_fit, parse_mod

output = phylo_fit(
    "hmrc.fa",
    tree="((human,(mouse,rat)),cow)",
    subst_mod="U2S",
    EM=True,
    precision="MED",
    non_overlapping=True,
    out_root="hmrc-u2s",
)

mod_lst = parse_mod("hmrc-u2s.mod")
print(mod_lst[0].rate_mat)
```

## Installation
Download and install PHAST first.

Install from PyPI:
```bash
pip install phasty
```
Or install from source after git clone:
```bash
cd phasty
pip install -e .
```
Run tests:
```bash
pip install -e .[dev]
python -m pytest --cov=phasty tests/
```
Uninstall:
```bash
pip uninstall phasty
```

## Notes
This package uses [Semantic Versioning](https://semver.org/).
