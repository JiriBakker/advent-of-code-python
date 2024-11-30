from main.day17 import day17a, day17b
from test.util import read_input, to_str_list

def test_day17a_example():
    assert 0 == day17a(to_str_list(""""""))

def test_day17a_actual():
    assert 0 == day17a(read_input(day = 17))

def test_day17b_example():
    assert 0 == day17b(to_str_list(""""""))

def test_day17b_actual():
    assert 0 == day17b(read_input(day = 17))