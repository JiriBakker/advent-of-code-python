from main.day25 import day25a
from test.util import read_input, to_str_list

def test_day25a_example():
    assert 0 == day25a(to_str_list(""""""))

def test_day25a_actual():
    assert 0 == day25a(read_input(day = 25))