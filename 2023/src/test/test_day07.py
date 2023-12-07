from main.day07 import day07a, day07b
from test.util import read_input

def test_day07a_example():
    assert 6440 == day07a(
        """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""".split("\n"))
    
def test_day07a_actual():
    assert 250898830 == day07a(read_input(day = 7))

def test_day07b_example():
    assert 5905 == day07b(
        """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""".split("\n"))

def test_day07b_actual():
    assert 252127335 == day07b(read_input(day = 7))