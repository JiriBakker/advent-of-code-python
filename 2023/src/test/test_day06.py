from main.day06 import day06a, day06b
from test.util import read_input, to_str_list

def test_day06a_example():
    assert 288 == day06a(to_str_list(
        """Time:      7  15   30
Distance:  9  40  200"""))
    
def test_day06a_actual():
    assert 138915 == day06a(read_input(day = 6))

def test_day06b_example():
    assert 71503 == day06b(to_str_list(
        """Time:      7  15   30
Distance:  9  40  200
"""))

def test_day06b_actual():
    assert 27340847 == day06b(read_input(day = 6))