from main.day10 import day10a, day10b
from test.util import read_input

def test_day10a_example():
    assert 8 == day10a(
        """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ""".split("\n"))
    
def test_day10a_actual():
    assert 6942 == day10a(read_input(day = 10))

def test_day10b_example1():
    assert 4 == day10b(
        """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........""".split("\n"))
    
def test_day10b_example2():
    assert 8 == day10b(
        """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...""".split("\n"))

def test_day10b_actual():
    assert 297 == day10b(read_input(day = 10))