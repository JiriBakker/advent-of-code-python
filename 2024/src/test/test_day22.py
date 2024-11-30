from main.day22 import day22a, day22b
from test.util import read_input, to_str_list

def test_day22a_example():
    assert 0 == day22a(to_str_list(""""""))

def test_day22a_actual():
    assert 0 == day22a(read_input(day = 22))

def test_day22b_example():
    assert 0 == day22b(to_str_list(""""""))

def test_day22b_actual():
    assert 0 == day22b(read_input(day = 22))