from functools import reduce
from typing import Callable
from main.util import first_or_none

def day03a(input: list[str]) -> int:
    parts = process_schematic(input, lambda char: not char.isnumeric() and char != ".")
    return sum(reduce(lambda acc, part: acc + part, parts.values(), []))

def day03b(input: list[str]) -> int:
    parts = process_schematic(input, lambda char : char == "*")
    return sum(map(lambda part: part[0] * part[1], filter(lambda part: len(part) == 2, parts.values())))

def process_schematic(input: list[str], is_symbol_match: Callable[[str], bool]) -> dict[tuple[int, int], list[int]]:
    def check_has_matching_symbol_adjacent(x: int, y: int) -> tuple[int, int] | None:
        return find_matching_neighbour(x, y, is_symbol_match, input)

    matching_parts = {}

    for y in range(0, len(input)):
        cur_nr = ""
        adjacent_symbol_pos = None

        def register_matched_symbol():
            if adjacent_symbol_pos != None and adjacent_symbol_pos not in matching_parts:                
                matching_parts[adjacent_symbol_pos] = []

        def store_matching_part():
            if len(cur_nr) > 0 and adjacent_symbol_pos != None:
                matching_parts[adjacent_symbol_pos].append(int(cur_nr))

        for x in range(0, len(input[y])):
            if input[y][x].isnumeric():
                nr = int(input[y][x])
                cur_nr = f"{cur_nr}{nr}"

                if adjacent_symbol_pos is None:
                    adjacent_symbol_pos = check_has_matching_symbol_adjacent(x, y)
                    register_matched_symbol()
                    
            else:
                store_matching_part()
                cur_nr = ""
                adjacent_symbol_pos = None

        store_matching_part()

    return matching_parts

def find_matching_neighbour(
    x: int, 
    y: int, 
    matcher: Callable[[str], bool], 
    grid: list[str]
) -> tuple[int, int] | None:
    neighbors = [
        (x-1, y-1), (x, y-1), (x+1, y-1), 
        (x-1, y  ),           (x+1, y  ), 
        (x-1, y+1), (x, y+1), (x+1, y+1)
    ]

    def is_valid_pos(pos: tuple[int, int]) -> bool:
        (x, y) = pos
        return x in range(0, len(grid[0])) and y in range(0, len(grid))

    return first_or_none(
        lambda neighbor: is_valid_pos(neighbor) and matcher(grid[neighbor[1]][neighbor[0]]),
        neighbors
    )