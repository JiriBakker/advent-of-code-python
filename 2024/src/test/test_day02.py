from main.day02 import day02a, day02b
from test.util import read_input, to_str_list

def test_day02a_example():
    assert 0 == day02a(to_str_list(""""""))

def test_day02a_actual():
    assert 0 == day02a(read_input(day = 2))

def test_day02b_example():
    assert 0 == day02b(to_str_list(""""""))

def test_day02b_actual():
    assert 0 == day02b(read_input(day = 2))

