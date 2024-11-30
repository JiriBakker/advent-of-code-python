from main.day06 import day06a, day06b
from test.util import read_input, to_str_list

def test_day06a_example():
    assert 0 == day06a(to_str_list(""""""))

def test_day06a_actual():
    assert 0 == day06a(read_input(day = 6))

def test_day06b_example():
    assert 0 == day06b(to_str_list(""""""))

def test_day06b_actual():
    assert 0 == day06b(read_input(day = 6))