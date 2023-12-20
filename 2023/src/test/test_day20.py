from main.day20 import day20a, day20b
from test.util import read_input, to_str_list

def test_day20a_example1():
    assert 32000000 == day20a(to_str_list(
        """broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a"""))
    
def test_day20a_example2():
    assert 11687500 == day20a(to_str_list(
        """broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output"""))


def test_day20a_actual():
    assert 944750144 == day20a(read_input(day = 20))

def test_day20b_actual():
    assert 222718819437131 == day20b(read_input(day = 20)) 