from main.day07 import day07a, day07b
from test.util import read_input, to_str_list

def test_day07a_example():
    assert 0 == day07a(to_str_list(""""""))

def test_day07a_actual():
    assert 0 == day07a(read_input(day = 7))

def test_day07b_example():
    assert 0 == day07b(to_str_list(""""""))

def test_day07b_actual():
    assert 0 == day07b(read_input(day = 7))