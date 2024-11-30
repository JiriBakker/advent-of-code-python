from main.day09 import day09a, day09b
from test.util import read_input, to_str_list

def test_day09a_example():
    assert 0 == day09a(to_str_list(""""""))

def test_day09a_actual():
    assert 0 == day09a(read_input(day = 9))

def test_day09b_example():
    assert 0 == day09b(to_str_list(""""""))

def test_day09b_actual():
    assert 0 == day09b(read_input(day = 9))