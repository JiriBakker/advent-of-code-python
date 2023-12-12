from main.day12 import day12a, day12b
from test.util import read_input

def test_day12a_custom1():
    assert 1 == day12a(
        """???.### 1,1,3""".split("\n"))
    
def test_day12a_custom2():
    assert 4 == day12a(
        """.??..??...?##. 1,1,3""".split("\n"))

def test_day12a_custom3():
    assert 1 == day12a(
        """?#?#?#?#?#?#?#? 1,3,1,6""".split("\n"))

def test_day12a_example():
    assert 21 == day12a(
        """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1""".split("\n"))
    
def test_day12a_actual():
    assert 6871 == day12a(read_input(day = 12))

def test_day12b_custom1():
    assert 1 == day12b(
        """???.### 1,1,3""".split("\n"))

def test_day12b_custom2():
    assert 16384 == day12b(
        """.??..??...?##. 1,1,3""".split("\n"))

def test_day12b_custom3():
    assert 1 == day12b(
        """?#?#?#?#?#?#?#? 1,3,1,6""".split("\n"))
    
def test_day12b_custom4():
    assert 16 == day12b(
        """????.#...#... 4,1,1""".split("\n"))
    
def test_day12b_custom5():
    assert 2500 == day12b(
        """????.######..#####. 1,6,5""".split("\n"))
    
def test_day12b_custom6():
    assert 506250 == day12b(
        """?###???????? 3,2,1""".split("\n"))
    
def test_day12b_custom7():
    assert 2787504 == day12b(
        """??#?#?#????.????#? 6,2,1,1""".split("\n"))

def test_day12b_example():
    assert 525152 == day12b(
        """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1""".split("\n"))
    
def test_day12b_actual():
    assert 2043098029844 == day12b(read_input(day = 12))