
from typing import Callable

def day09a(input: list[str]) -> int:
    sequences = parse_histories(input)
    return sum(map(lambda sequence: extrapolate_history(sequence, lambda delta: delta, lambda a, b: a + b), sequences))

def day09b(input: list[str]) -> int:
    histories = parse_histories(input)
    return sum(map(lambda sequence: extrapolate_history(sequence, lambda delta: list(reversed(delta)), lambda a, b: a - b), histories))

def extrapolate_history(
    history: list[int], 
    map_delta: Callable[[list[int]], list[int]],
    extrapolate: Callable[[int, int], int]
) -> int:
    deltas = [history]
    while True:
        delta = get_deltas(deltas[-1])
        deltas.append(delta)
        if is_zeroes(delta):
            break

    mapped_deltas = list(map(lambda delta: map_delta(delta), deltas))

    delta = mapped_deltas[-2][-1]
    for i in range(len(mapped_deltas) - 3, -1, -1):
        next_value = extrapolate(mapped_deltas[i][-1], delta)
        mapped_deltas[i].append(next_value)
        delta = mapped_deltas[i][-1]

    return mapped_deltas[0][-1]

def parse_histories(input: list[str]) -> list[list[int]]:
    return list(map(lambda line: list(map(lambda nr: int(nr), line.split(" "))), input))

def get_deltas(sequence: list[int]) -> list[int]:
    return list(map(lambda i: sequence[i] - sequence[i - 1], range(1, len(sequence))))

def is_zeroes(sequence: list[int]) -> bool:
    return all(map(lambda nr: nr == 0, sequence))