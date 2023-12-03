from functools import reduce
from typing import Callable

def day03a(input: list[str]) -> int:
    parts = process_schematic(input, lambda char: not char.isnumeric() and char != ".")
    return sum(reduce(lambda acc, part: acc + part, parts.values(), []))

def day03b(input: list[str]) -> int:
    parts = process_schematic(input, lambda char : char == "*")
    return sum(map(lambda part: part[0] * part[1], filter(lambda part: len(part) == 2, parts.values())))

def process_schematic(input: list[str], is_symbol_match: Callable[[str], bool]) -> dict[tuple[int, int], list[int]]:
    def check_has_symbol_adjacent(x: int, y: int) -> tuple[int, int] | None:
        return has_matching_neighbour(x, y, is_symbol_match, input)

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
                    adjacent_symbol_pos = check_has_symbol_adjacent(x, y)
                    register_matched_symbol()
                    
            else:
                store_matching_part()
                cur_nr = ""
                adjacent_symbol_pos = None

        store_matching_part()

    return matching_parts

def has_matching_neighbour(x, y, matcher: Callable[[str], bool], grid: list[str]) -> tuple[int, int] | None:
    neighbors = [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]

    for (x, y) in neighbors:
        if x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid) and matcher(grid[y][x]):
            return (x, y)
        
    return None