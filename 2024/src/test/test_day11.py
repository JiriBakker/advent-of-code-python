from main.day11 import day11a, day11b
from test.util import read_input, to_str_list

def test_day11a_example():
    assert 0 == day11a(to_str_list(""""""))

def test_day11a_actual():
    assert 0 == day11a(read_input(day = 11))

def test_day11b_example():
    assert 0 == day11b(to_str_list(""""""))

def test_day11b_actual():
    assert 0 == day11b(read_input(day = 11))