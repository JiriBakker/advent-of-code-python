from main.day05 import day05a, day05b
from test.util import read_input, to_str_list

def test_day05a_example():
    assert 0 == day05a(to_str_list(""""""))

def test_day05a_actual():
    assert 0 == day05a(read_input(day = 5))

def test_day05b_example():
    assert 0 == day05b(to_str_list(""""""))

def test_day05b_actual():
    assert 0 == day05b(read_input(day = 5))