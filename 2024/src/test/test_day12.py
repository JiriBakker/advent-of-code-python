from main.day12 import day12a, day12b
from test.util import read_input, to_str_list

def test_day12a_example():
    assert 0 == day12a(to_str_list(""""""))

def test_day12a_actual():
    assert 0 == day12a(read_input(day = 12))

def test_day12b_example():
    assert 0 == day12b(to_str_list(""""""))

def test_day12b_actual():
    assert 0 == day12b(read_input(day = 12))