from functools import reduce
import sys
from typing import Callable

def min_of[T](selector: Callable[[T], int], values: list[T]) -> int:
    return reduce(lambda min, value: min if min < selector(value) else selector(value), values, sys.maxsize)

def max_of[T](selector: Callable[[T], int], values: list[T]) -> int:
    return reduce(lambda max, value: max if max > selector(value) else selector(value), values, -sys.maxsize)

def min_by_or_none[T](selector: Callable[[T], int], values: list[T]) -> T | None:
    def reducer(acc: tuple[int, T | None], value: T) -> tuple[int, T | None]:
        return acc if acc[0] < selector(value) else (selector(value), value)
    result = reduce(reducer, values, (sys.maxsize, None))
    return result[1]

def max_by_or_none[T](selector: Callable[[T], int], values: list[T]) -> T | None:
    def reducer(acc: tuple[int, T | None], value: T) -> tuple[int, T | None]:
        return acc if acc[0] > selector(value) else (selector(value), value)
    result = reduce(reducer, values, (-sys.maxsize, None))
    return result[1]

def first_or_none[T](filter: Callable[[T], bool], iterable: list[T]) -> T | None:
    for item in iterable:
        if filter(item):
            return item
    return None

def any[T](filter: Callable[[T], bool], iterable: list[T]) -> bool:
    return first_or_none(filter, iterable) != None
