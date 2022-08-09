from phasty import wrapper


def test_format_options():
    assert wrapper._format_options(
        {
            "tree": "((human,chimp),(mouse,rat))",
            "subst_mod": "JC69",
            "EM": True,
            "nrates": 4,
            "non_overlapping": False,
        }
    ) == [
        "--tree",
        "((human,chimp),(mouse,rat))",
        "--subst-mod",
        "JC69",
        "--EM",
        "--nrates",
        "4",
    ]


def test_phylofit():
    assert wrapper.phylofit() is None
