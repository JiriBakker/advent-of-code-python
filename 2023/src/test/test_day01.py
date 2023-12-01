from main.day01 import day01a, day01b
from test.util import read_input

def test_day01a_example():
    assert 142 == day01a(
        """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""".split("\n"))
    
def test_day01a_actual():
    assert 54159 == day01a(read_input(day = 1))


def test_day01b_example():
    assert 281 == day01b(
        """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""".split("\n"))
    
def test_day01b_actual():
    assert 53866 == day01b(read_input(day = 1))