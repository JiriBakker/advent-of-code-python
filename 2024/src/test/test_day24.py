from main.day24 import day24a, day24b
from test.util import read_input, to_str_list

def test_day24a_example():
    assert 0 == day24a(to_str_list(""""""))

def test_day24a_actual():
    assert 0 == day24a(read_input(day = 24))

def test_day24b_example():
    assert 0 == day24b(to_str_list(""""""))

def test_day24b_actual():
    assert 0 == day24b(read_input(day = 24))