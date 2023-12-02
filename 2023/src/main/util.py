from functools import reduce
import sys
from typing import Callable

def min_by[T](selector: Callable[[T], int], values: list[T]) -> int:
    return reduce(lambda min, value: min if min < selector(value) else selector(value), values, sys.maxsize)

def max_by[T](selector: Callable[[T], int], values: list[T]) -> int:
    return reduce(lambda max, value: max if max > selector(value) else selector(value), values, -sys.maxsize)