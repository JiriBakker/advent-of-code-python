from main.day03 import day03a, day03b
from test.util import read_input, to_str_list

def test_day03a_example():
    assert 0 == day03a(to_str_list(""""""))

def test_day03a_actual():
    assert 0 == day03a(read_input(day = 3))

def test_day03b_example():
    assert 0 == day03b(to_str_list(""""""))

def test_day03b_actual():
    assert 0 == day03b(read_input(day = 3))