from main.day14 import day14a, day14b
from test.util import read_input, to_str_list

def test_day14a_example():
    assert 136 == day14a(to_str_list(
        """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""))
    
def test_day14a_actual():
    assert 108935 == day14a(read_input(day = 14))

def test_day14b_example():
    assert 64 == day14b(to_str_list(
        """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""))
    
def test_day14b_actual():
    assert 100876 == day14b(read_input(day = 14))