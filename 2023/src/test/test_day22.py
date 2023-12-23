from main.day22 import day22a, day22b
from test.util import read_input, to_str_list
import pytest

def test_day22a_example():
    assert 5 == day22a(to_str_list(
        """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9"""))
    
@pytest.mark.skip(reason="Too slow (11s)")
def test_day22a_actual():
    assert 3605 == day22a(read_input(day = 22))

def test_day22b_example():
    assert 7 == day22b(to_str_list(
        """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9"""))
    
def test_day22b_custom():
    assert 1 == day22b(to_str_list(
        """1,0,1~1,2,1
1,2,1~1,4,1
1,1,2~1,3,2
1,3,2~1,5,2"""))

@pytest.mark.skip(reason="Too slow (~2m30s)")
def test_day22b_actual():
    assert 60558 == day22b(read_input(day = 22)) 