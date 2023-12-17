from main.day15 import day15a, day15b
from test.util import read_input, to_str_list

def test_day15a_example1():
    assert 52 == day15a(to_str_list(
        """HASH"""))

def test_day15a_example2():
    assert 1320 == day15a(to_str_list(
        """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""))
    
def test_day15a_actual():
    assert 516070 == day15a(read_input(day = 15))

def test_day15b_example():
    assert 145 == day15b(to_str_list(
        """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""))
    
def test_day15b_actual():
    assert 244981 == day15b(read_input(day = 15))