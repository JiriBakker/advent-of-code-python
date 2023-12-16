from main.day16 import day16a, day16b
from test.util import read_input

def test_day16a_example():
    assert 46 == day16a(
        """.|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|....""".split("\n"))

def test_day16a_actual():
    assert 6855 == day16a(read_input(day = 16))

def test_day16b_example():
    assert 51 == day16b(
        """.|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|....""".split("\n"))
    
def test_day16b_actual():
    assert 7513 == day16b(read_input(day = 16)) 