import re
from typing import Callable
from main.util import max_by

def day03a(input: list[str]) -> int:
    part_numbers = parse_schematic(input)
    return sum(part_numbers)

def day03b(input: list[str]) -> int:
    gear_ratios = parse_gear_ratios(input)
    return sum(gear_ratios)

def parse_gear_ratios(input: list[str]) -> list[int]:
    def find_adjacent_gear_pos(x: int, y: int) -> tuple[int, int] | None:
        def is_gear(char: str) -> bool:
            return char == "*"
        return has_matching_neighbour(x, y, is_gear, input)

    gears = {}
    
    for y in range(0, len(input)):
        line = input[y]
        cur_nr = ""
        gear_pos = None
        for x in range(0, len(line)):
            if line[x].isnumeric():
                nr = int(line[x])
                cur_nr = f"{cur_nr}{nr}"
                if gear_pos is None:
                    gear_pos = find_adjacent_gear_pos(x, y)
                    if gear_pos != None and gear_pos not in gears:
                        gears[gear_pos] = []

            else:
                if len(cur_nr) > 0 and gear_pos != None:
                    gears[gear_pos].append(int(cur_nr))
                    
                cur_nr = ""
                gear_pos = None

        if len(cur_nr) > 0 and gear_pos != None:
            gears[gear_pos].append(int(cur_nr))

    return list(map(lambda gear: gear[0] * gear[1], filter(lambda gear: len(gear) == 2, gears.values())))


def parse_schematic(input: list[str]) -> list[int]:
    def check_has_symbol_adjacent(x: int, y: int) -> bool:
        def is_symbol(char: str) -> bool:
            return not char.isnumeric() and char != "."
        return has_matching_neighbour(x, y, is_symbol, input) != None

    part_numbers = []
    for y in range(0, len(input)):
        line = input[y]
        cur_nr = ""
        has_symbol_adjacent = False
        for x in range(0, len(line)):
            if line[x].isnumeric():
                nr = int(line[x])
                cur_nr = f"{cur_nr}{nr}"
                has_symbol_adjacent = has_symbol_adjacent or check_has_symbol_adjacent(x, y)
            else:
                if len(cur_nr) > 0 and has_symbol_adjacent:
                    part_numbers.append(int(cur_nr))
                cur_nr = ""
                has_symbol_adjacent = False

        if len(cur_nr) > 0 and has_symbol_adjacent:
            part_numbers.append(int(cur_nr))

    return part_numbers

def has_matching_neighbour(x, y, matcher: Callable[[str], bool], grid: list[str]) -> tuple[int, int] | None:
    neighbors = [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]

    for (x, y) in neighbors:
        if x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid) and matcher(grid[y][x]):
            return (x, y)
        
    return None