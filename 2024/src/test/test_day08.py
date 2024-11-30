from main.day08 import day08a, day08b
from test.util import read_input, to_str_list

def test_day08a_example():
    assert 0 == day08a(to_str_list(""""""))

def test_day08a_actual():
    assert 0 == day08a(read_input(day = 8))

def test_day08b_example():
    assert 0 == day08b(to_str_list(""""""))

def test_day08b_actual():
    assert 0 == day08b(read_input(day = 8))