"""A module wraps the major programs of PHAST."""

import re
import subprocess
from itertools import chain


def _format_options(kwargs: dict):
    options = []
    for k, v in kwargs.items():
        s = f"--{k.replace('_', '-')}"
        if isinstance(v, bool):
            if v:
                options.append(s)
        elif isinstance(v, list):
            options.extend(chain.from_iterable(zip([s] * len(v), v)))
        else:
            options.extend([s, str(v)])
    return options


def _create_function(name: str):
    def command(*args, **kwargs):
        """Run command and return the stdout.

        Args:
            args: non-option argument(s) of the command.
            kwargs: options and arguments of the command.

        Returns:
            A string of the stdout.
        """
        options = _format_options(kwargs)
        command = [name] + options + list(args)
        try:
            proc = subprocess.run(
                command, capture_output=True, check=True, text=True
            )
            print(proc.args, proc.stderr, sep="\n")
        except Exception as err:
            # not very useful to raise exception here
            print(err.stderr if hasattr(err, "stderr") else repr(err))
        return proc.stdout if "proc" in locals() else ""

    return command


def _snake_case(name: str):
    return re.sub(r"([A-Z]+)", r"_\1", name).lower()


_COMMANDS = [
    "all_dists",
    "base_evolve",
    "chooseLines",
    "clean_genes",
    "consEntropy",
    "convert_coords",
    "display_rate_matrix",
    "dless",
    "dlessP",
    "dmTranslateToRealigned",
    "dmcompare",
    "dmcondition",
    "dmotif",
    "dmsample",
    "dmsimulate",
    "draw_tree",
    "eval_predictions",
    "exoniphy",
    "hmm_train",
    "hmm_tweak",
    "hmm_view",
    "indelFit",
    "indelHistory",
    "maf_parse",
    "makeHKY",
    "modFreqs",
    "msa_diff",
    "msa_split",
    "msa_view",
    "pbsDecode",
    "pbsEncode",
    "pbsScoreMatrix",
    "pbsTrain",
    "phastBias",
    "phastCons",
    "phastMotif",
    "phastOdds",
    "phyloBoot",
    "phyloFit",
    "phyloP",
    "prequel",
    "refeature",
    "stringiphy",
    "treeGen",
    "tree_doctor",
]

for _name in _COMMANDS:
    globals()[_snake_case(_name)] = _create_function(_name)

__all__ = [name for name in dir() if not name.startswith("_")]
