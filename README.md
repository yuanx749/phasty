# phasty
A Python interface for PHAST (phylogenetic analysis with space/time models).

## Description
[PHAST](http://compgen.cshl.edu/phast/) is a package consisting of command-line programs for comparative genomics. It supports several nucleotide substitution models. This package provides Python wrappers for some major programs so that it is easier to integrate them into complicated workflows. It can also parse some file formats to more computer-friendly forms to help downstream analysis.

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
Uninstall:
```bash
pip uninstall phasty
```

## Notes
This package uses [Semantic Versioning](https://semver.org/).
