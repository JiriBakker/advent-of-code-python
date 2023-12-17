from main.day17 import day17a, day17b
from test.util import read_input, to_str_list
import pytest

def test_day17a_example():
    assert 102 == day17a(to_str_list(
        """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""))

@pytest.mark.skip(reason="Too slow")
def test_day17a_actual():
    assert 1128 == day17a(read_input(day = 17))

def test_day17b_example1():
    assert 94 == day17b(to_str_list(
        """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""))
    
def test_day17b_example2():
    assert 71 == day17b(to_str_list(
        """111111111111
999999999991
999999999991
999999999991
999999999991"""))

@pytest.mark.skip(reason="Too slow")
def test_day17b_actual():
    assert 1268 == day17b(read_input(day = 17)) 