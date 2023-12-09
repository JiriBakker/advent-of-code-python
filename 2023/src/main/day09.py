from main.util import sum_by

def day09a(input: list[str]) -> int:
    histories = parse_histories(input)
    return sum_by(lambda history: extrapolate(history, -1, 1), histories)

def day09b(input: list[str]) -> int:
    histories = parse_histories(input)
    return sum_by(lambda history: extrapolate(history, 0, -1), histories)

def extrapolate(history: list[int], extrapolate_index: int, sign: int) -> int:
    if is_stable(history):
        return history[0]

    return (
        history[extrapolate_index] + 
        sign * extrapolate(get_deltas(history), extrapolate_index, sign)
    )

def get_deltas(history: list[int]) -> list[int]:
    return list(map(lambda i: history[i] - history[i - 1], range(1, len(history))))

def is_stable(history: list[int]) -> bool:
    return all(map(lambda nr: nr == history[0], history))

def parse_histories(input: list[str]) -> list[list[int]]:
    return list(map(lambda line: list(map(lambda nr: int(nr), line.split(" "))), input))