from main.day04 import day04a, day04b
from test.util import read_input, to_str_list

def test_day04a_example():
    assert 0 == day04a(to_str_list(""""""))

def test_day04a_actual():
    assert 0 == day04a(read_input(day = 4))

def test_day04b_example():
    assert 0 == day04b(to_str_list(""""""))

def test_day04b_actual():
    assert 0 == day04b(read_input(day = 4))