from main.day03 import day03a, day03b
from test.util import read_input

def test_day03a_example():
    assert 4361 == day03a(
        """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".split("\n"))
    
def test_day03a_actual():
    assert 544664 == day03a(read_input(day = 3))

def test_day03b_example():
    assert 467835 == day03b(
        """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".split("\n"))
    
def test_day03b_actual():
    assert 84495585 == day03b(read_input(day = 3))