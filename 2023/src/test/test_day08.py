from main.day08 import day08a, day08b
from test.util import read_input

def test_day08a_example1():
    assert 2 == day08a(
        """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)""".split("\n"))
    
def test_day08a_example2():
    assert 6 == day08a(
        """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)""".split("\n"))
    
def test_day08a_actual():
    assert 17621 == day08a(read_input(day = 8))

def test_day08b_example():
    assert 6 == day08b(
        """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)""".split("\n"))

def test_day08b_actual():
    assert 20685524831999 == day08b(read_input(day = 8))