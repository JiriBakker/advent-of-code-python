from main.day21 import day21a, day21b
from test.util import read_input, to_str_list

def test_day21a_example():
    assert 0 == day21a(to_str_list(""""""))

def test_day21a_actual():
    assert 0 == day21a(read_input(day = 21))

def test_day21b_example():
    assert 0 == day21b(to_str_list(""""""))

def test_day21b_actual():
    assert 0 == day21b(read_input(day = 21))