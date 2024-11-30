from main.day20 import day20a, day20b
from test.util import read_input, to_str_list

def test_day20a_example():
    assert 0 == day20a(to_str_list(""""""))

def test_day20a_actual():
    assert 0 == day20a(read_input(day = 20))

def test_day20b_example():
    assert 0 == day20b(to_str_list(""""""))

def test_day20b_actual():
    assert 0 == day20b(read_input(day = 20))