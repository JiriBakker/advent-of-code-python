from main.day24 import day24a, day24b
from test.util import read_input, to_str_list

def test_day24a_example():
    assert 2 == day24a(to_str_list(
        """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3"""), min_coor = 7, max_coor = 27)
    
def test_day24a_actual():
    assert 16050 == day24a(read_input(day = 24))

def test_day24b_actual():
    assert 669042940632377 == day24b(read_input(day = 24)) 