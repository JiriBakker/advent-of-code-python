from main.day11 import day11a, day11b
from test.util import read_input, to_str_list

def test_day11a_example():
    assert 374 == day11a(to_str_list(
        """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""))
    
def test_day11a_actual():
    assert 9521550 == day11a(read_input(day = 11))

def test_day11b_example1():
    assert 1030 == day11b(to_str_list(
        """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""), delta = 10)
    
def test_day11b_example2():
    assert 8410 == day11b(to_str_list(
        """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""), delta = 100)

def test_day11b_actual():
    assert 298932923702 == day11b(read_input(day = 11))