from main.day18 import day18a, day18b
from test.util import read_input, to_str_list
import pytest

def test_day18a_example():
    assert 62 == day18a(to_str_list(
        """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""))

def test_day18a_actual():
    assert 48652 == day18a(read_input(day = 18))

@pytest.mark.skip(reason="Too slow (4s)")
def test_day18b_example():
    assert 952408144115 == day18b(to_str_list(
        """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""))

@pytest.mark.skip(reason="Too slow (~1m25s)")
def test_day18b_actual():
    assert 45757884535661 == day18b(read_input(day = 18)) 