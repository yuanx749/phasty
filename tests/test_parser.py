from phasty import parse_mod


def test_parse_mod():
    mod = parse_mod("tests/phyloFit.mod")[0]
    assert mod.alphabet[0] == "A"
    assert mod.order == 0
    assert type(mod.background[0]) is float
    assert mod.rate_mat.shape == (4, 4)
