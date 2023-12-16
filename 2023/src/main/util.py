from functools import reduce
from typing import Callable, Sized
import sys

# Collections
def min_of[T](selector: Callable[[T], int], values: list[T]) -> int:
    return reduce(lambda min, value: min if min < selector(value) else selector(value), values, sys.maxsize)

def max_of[T](selector: Callable[[T], int], values: list[T]) -> int:
    return reduce(lambda max, value: max if max > selector(value) else selector(value), values, -sys.maxsize)

def min_by_or_none[T](selector: Callable[[T], int], values: list[T]) -> T | None:
    def reducer(acc: tuple[int, T | None], value: T) -> tuple[int, T | None]:
        result = selector(value)
        return acc if acc[0] < result else (result, value)
    result = reduce(reducer, values, (sys.maxsize, None))
    return result[1]

def max_by_or_none[T](selector: Callable[[T], int], values: list[T]) -> T | None:
    def reducer(acc: tuple[int, T | None], value: T) -> tuple[int, T | None]:
        result = selector(value)
        return acc if acc[0] > result else (result, value)
    result = reduce(reducer, values, (-sys.maxsize, None))
    return result[1]

def min_by[T](selector: Callable[[T], int], values: list[T]) -> T:
    min = min_by_or_none(selector, values)
    if min == None:
        raise Exception("No min found (empty list?)")
    return min

def max_by[T](selector: Callable[[T], int], values: list[T]) -> T:
    max = max_by_or_none(selector, values)
    if max == None:
        raise Exception("No max found (empty list?)")
    return max

def sum_by[T](selector: Callable[[T], int], values: list[T]) -> int:
    return reduce(lambda acc, value: acc + selector(value), values, 0)

def first_or_none[T](filter: Callable[[T], bool], iterable: list[T]) -> T | None:
    for item in iterable:
        if filter(item):
            return item
    return None

def any[T](filter: Callable[[T], bool], iterable: list[T]) -> bool:
    return first_or_none(filter, iterable) != None

def none[T](filter: Callable[[T], bool], iterable: list[T]) -> bool:
    return first_or_none(filter, iterable) == None

def all[T](filter: Callable[[T], bool], iterable: list[T]) -> bool:
    return first_or_none(lambda it: filter(it) == False, iterable) == None

def filter_empty[T : Sized](input: list[T]) -> list[T]:
    return list(filter(lambda item: len(item) > 0, input))

def manhattan_distance(x1: int, y1: int, x2: int, y2: int) -> int:
    return abs(x1 - x2) + abs(y1 - y2)

def repeat(func: Callable[[], None], times: int) -> None:
    for _ in range(0, times):
        func()