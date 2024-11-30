from main.day19 import day19a, day19b
from test.util import read_input, to_str_list

def test_day19a_example():
    assert 0 == day19a(to_str_list(""""""))

def test_day19a_actual():
    assert 0 == day19a(read_input(day = 19))

def test_day19b_example():
    assert 0 == day19b(to_str_list(""""""))

def test_day19b_actual():
    assert 0 == day19b(read_input(day = 19))