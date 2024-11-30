from main.day14 import day14a, day14b
from test.util import read_input, to_str_list

def test_day14a_example():
    assert 0 == day14a(to_str_list(""""""))

def test_day14a_actual():
    assert 0 == day14a(read_input(day = 14))

def test_day14b_example():
    assert 0 == day14b(to_str_list(""""""))

def test_day14b_actual():
    assert 0 == day14b(read_input(day = 14))