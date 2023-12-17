from main.day09 import day09a, day09b
from test.util import read_input, to_str_list

def test_day09a_example():
    assert 114 == day09a(to_str_list(
        """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""))
    
def test_day09a_actual():
    assert 1898776583 == day09a(read_input(day = 9))

def test_day09b_example():
    assert 2 == day09b(to_str_list(
        """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""))

def test_day09b_actual():
    assert 1100 == day09b(read_input(day = 9))