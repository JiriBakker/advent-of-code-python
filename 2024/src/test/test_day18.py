from main.day18 import day18a, day18b
from test.util import read_input, to_str_list

def test_day18a_example():
    assert 0 == day18a(to_str_list(""""""))

def test_day18a_actual():
    assert 0 == day18a(read_input(day = 18))

def test_day18b_example():
    assert 0 == day18b(to_str_list(""""""))

def test_day18b_actual():
    assert 0 == day18b(read_input(day = 18))