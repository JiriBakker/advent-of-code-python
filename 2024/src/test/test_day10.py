from main.day10 import day10a, day10b
from test.util import read_input, to_str_list

def test_day10a_example():
    assert 0 == day10a(to_str_list(""""""))

def test_day10a_actual():
    assert 0 == day10a(read_input(day = 10))

def test_day10b_example():
    assert 0 == day10b(to_str_list(""""""))

def test_day10b_actual():
    assert 0 == day10b(read_input(day = 10))