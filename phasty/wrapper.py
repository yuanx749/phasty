"""A module wraps the major programs of PHAST."""

import subprocess


def _format_options(kwargs: dict):
    options = []
    for k, v in kwargs.items():
        if isinstance(v, bool):
            if v:
                options.append(f"--{k.replace('_', '-')}")
        else:
            options.extend([f"--{k.replace('_', '-')}", str(v)])
    return options


def phylofit(msa_fname: str = "", **kwargs):
    """Run phyloFit: fitting of phylogenetic models to aligned DNA sequences.

    Refer to http://compgen.cshl.edu/phast/help-pages/phyloFit.txt for kwargs.
    """
    options = _format_options(kwargs)
    command = ["phyloFit"] + options + [msa_fname]
    try:
        proc = subprocess.run(
            command, capture_output=True, check=True, text=True
        )
        print(proc.args, proc.stderr, sep="\n")
    except Exception as err:
        print(err.stderr if hasattr(err, "stderr") else repr(err))
    return
