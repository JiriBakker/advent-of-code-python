from functools import reduce
from math import ceil, floor, sqrt
from main.util import filter_empty

def day06a(input: list[str]) -> int:
    races = parse_races(input)
    nrs = list(map(lambda race: count_nr_of_ways_to_beat_record(race[0], race[1]), races))
    return reduce(lambda acc, nr: acc * nr, nrs, 1)

def day06b(input: list[str]) -> int:
    (time, record) = parse_kerned_race(input)
    return count_nr_of_ways_to_beat_record(time, record)

def parse_races(input: list[str]) -> list[tuple[int, int]]:
    (times, records) = map(lambda line: map(lambda nr: int(nr), filter_empty(line.split(" ")[1:])), input)
    return list(zip(times, records))

def parse_kerned_race(input: list[str]) -> tuple[int, int]:
    time = int(input[0].replace(" ", "")[5:])
    record = int(input[1].replace(" ", "")[9:])
    return (time, record)

def count_nr_of_ways_to_beat_record(time: int, record: int) -> int:
    target = record + 1
    x1 = (-time + sqrt(time**2 - 4*target)) / -2
    x2 = (-time - sqrt(time**2 - 4*target)) / -2
    return int(floor(x2)) - int(ceil(x1)) + 1