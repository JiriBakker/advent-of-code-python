from main.day01 import day01a, day01b
from test.util import read_input, to_str_list

def test_day01a_example():
    assert 0 == day01a(to_str_list(""""""))

def test_day01a_actual():
    assert 0 == day01a(read_input(day = 1))

def test_day01b_example():
    assert 0 == day01b(to_str_list(""""""))

def test_day01b_actual():
    assert 0 == day01b(read_input(day = 1))