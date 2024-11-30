from main.day15 import day15a, day15b
from test.util import read_input, to_str_list

def test_day15a_example():
    assert 0 == day15a(to_str_list(""""""))

def test_day15a_actual():
    assert 0 == day15a(read_input(day = 15))

def test_day15b_example():
    assert 0 == day15b(to_str_list(""""""))

def test_day15b_actual():
    assert 0 == day15b(read_input(day = 15))