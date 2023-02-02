from phasty import parser


def test_parse_mod():
    mod = parser.parse_mod("tests/phyloFit.mod")[0]
    assert mod.alphabet[0] == "A"
    assert mod.order == 0
    assert isinstance(mod.background[0], float)
    assert mod.rate_mat.shape == (4, 4)
