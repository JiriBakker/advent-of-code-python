from main.day13 import day13a, day13b
from test.util import read_input, to_str_list

def test_day13a_example():
    assert 0 == day13a(to_str_list(""""""))

def test_day13a_actual():
    assert 0 == day13a(read_input(day = 13))

def test_day13b_example():
    assert 0 == day13b(to_str_list(""""""))

def test_day13b_actual():
    assert 0 == day13b(read_input(day = 13))