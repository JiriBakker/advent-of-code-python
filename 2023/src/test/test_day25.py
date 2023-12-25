from main.day25 import day25a
from test.util import read_input, to_str_list

def test_day25a_example():
    assert 94 == day25a(to_str_list(
        """jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr"""))
    
# def test_day25a_actual():
#     assert 16050 == day25a(read_input(day = 25))
