from functools import reduce
import sys
from typing import Callable

def min_by[T](selector: Callable[[T], int], values: list[T]) -> int:
    return reduce(lambda min, value: min if min < selector(value) else selector(value), values, sys.maxsize)

def max_by[T](selector: Callable[[T], int], values: list[T]) -> int:
    return reduce(lambda max, value: max if max > selector(value) else selector(value), values, -sys.maxsize)

def any[T](filter: Callable[[T], bool], iterable: list[T]) -> bool:
    for item in iterable:
        if filter(item):
            return True
    return False

def firstOrNone[T](filter: Callable[[T], bool], iterable: list[T]) -> T | None:
    for item in iterable:
        if filter(item):
            return item
    return None