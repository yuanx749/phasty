from phasty import wrapper


def test_format_options():
    assert wrapper._format_options(
        {
            "tree": "((human,chimp),(mouse,rat))",
            "subst_mod": "JC69",
            "EM": True,
            "nrates": 4,
            "non_overlapping": False,
            "alt_model": ["human:ratematrix", "mouse:ratematrix"],
        }
    ) == [
        "--tree",
        "((human,chimp),(mouse,rat))",
        "--subst-mod",
        "JC69",
        "--EM",
        "--nrates",
        "4",
        "--alt-model",
        "human:ratematrix",
        "--alt-model",
        "mouse:ratematrix",
    ]


def test_phylofit():
    assert isinstance(wrapper.phylofit(), str)
