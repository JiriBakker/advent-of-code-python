from typing import Sequence
from main.util import repeat

def day14a(input: list[str]) -> int:
    grid = list(map(lambda line: list(line), input))
    tilt(grid, range(0, len(grid)), range(0, len(grid)), 0, -1)
    return compute_load(grid)

def day14b(input: list[str]) -> int:
    grid = list(map(lambda line: list(line), input))

    def grid_hash() -> str:
        return "".join(map(lambda line: "".join(line), grid))
    
    seen = { f"{grid_hash()}": 0}

    cycle = 0
    while True:
        cycle += 1
        tilt_cycle(grid)
        
        grid_hash_value = grid_hash()
        if grid_hash_value in seen:
            cycle_length = cycle - seen[grid_hash_value]
            cycle_delta = (1000000000 - cycle) % cycle_length
            repeat(lambda: tilt_cycle(grid), cycle_delta)
            return compute_load(grid)

        seen[grid_hash_value] = cycle

def tilt_cycle(grid: list[list[str]]):
    tilt(grid, range(0, len(grid)), range(0, len(grid)), 0, -1)
    tilt(grid, range(0, len(grid)), range(0, len(grid)), -1, 0)
    tilt(grid, range(0, len(grid)), range(len(grid[0]) - 1, -1, -1), 0, 1)
    tilt(grid, range(len(grid) - 1, -1, -1), range(0, len(grid)), 1, 0)
    
def tilt(grid: list[list[str]], x_range: Sequence[int], y_range: Sequence[int], x_delta: int, y_delta: int):
    for y in y_range:
        for x in x_range:
            if grid[y][x] == "O":
                (empty_x, empty_y) = find_empty(x, y, x_delta, y_delta, grid)
                grid[y][x] = "."
                grid[empty_y][empty_x] = "O"

def find_empty(x_start: int, y_start: int, x_delta: int, y_delta: int, grid: list[list[str]]) -> tuple[int, int]:
    x = x_start
    y = y_start
    while True:
        next_x = x + x_delta
        next_y = y + y_delta
        if next_x < 0 or next_y < 0 or next_x >= len(grid[0]) or next_y >= len(grid) or grid[next_y][next_x] != ".":
            return (x, y)
        x = next_x
        y = next_y

def compute_load(grid: list[list[str]]) -> int:
    load = 0
    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if grid[y][x] == "O":
                load += len(grid) - y
    return load