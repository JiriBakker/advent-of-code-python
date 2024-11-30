from main.day23 import day23a, day23b
from test.util import read_input, to_str_list

def test_day23a_example():
    assert 0 == day23a(to_str_list(""""""))

def test_day23a_actual():
    assert 0 == day23a(read_input(day = 23))

def test_day23b_example():
    assert 0 == day23b(to_str_list(""""""))

def test_day23b_actual():
    assert 0 == day23b(read_input(day = 23))