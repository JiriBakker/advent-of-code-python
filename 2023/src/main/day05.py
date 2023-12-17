import sys

def day05a(input: list[str]) -> int:
    (seeds, mappings) = parse_almanac(input)
    return find_lowest_location_with_seeds(seeds, mappings)

def day05b(input: list[str]) -> int:
    (seeds, mappings) = parse_almanac(input)
    seed_ranges = list(zip(*(iter(seeds),) * 2))
    return find_lowest_location_with_seed_ranges(seed_ranges, list(reversed(mappings)))

class AlmanacMapping:
    def __init__(self):
        self.ranges: list[tuple[int,int,int]] = []

    def add_range(self, destStart: int, srcStart: int, rangeLength: int):
        self.ranges.append((destStart, srcStart, rangeLength))

    def map(self, source: int) -> int:
        for (destStart, srcStart, rangeLength) in self.ranges:
            if source in range(srcStart, srcStart + rangeLength):
                return destStart + source - srcStart
            
        return source
    
    def inverse_map(self, source: int) -> int:
        for (destStart, srcStart, rangeLength) in self.ranges:
            if source in range(destStart, destStart + rangeLength):
                return srcStart + source - destStart
            
        return source

def parse_almanac(input: list[str]) -> tuple[list[int], list[AlmanacMapping]]:
    seeds = list(map(lambda nr: int(nr), input[0].split(":")[1].strip().split(" ")))

    mappings: list[AlmanacMapping] = []

    cur_mapping = AlmanacMapping()
    for line in input[2:]:
        if len(line) == 0:
            continue

        if line.split(" ")[1] == "map:":
            mappings.append(cur_mapping)
            cur_mapping = AlmanacMapping()
            continue

        (destStart, srcStart, rangeLength) = map(lambda nr: int(nr), line.split(" "))
        cur_mapping.add_range(destStart, srcStart, rangeLength)

    mappings.append(cur_mapping)

    return (seeds, mappings)

def find_lowest_location_with_seeds(seeds: list[int], mappings: list[AlmanacMapping]) -> int:
    min_location = sys.maxsize

    for seed in seeds:
        cur_value = seed
        for mapping in mappings:
            cur_value = mapping.map(cur_value)

        min_location = min(min_location, cur_value)

    return min_location

def find_lowest_location_with_seed_ranges(seed_ranges: list[tuple[int, int]], mappings: list[AlmanacMapping]) -> int:
    location = 0
    while True:
        cur_value = location
        for mapping in mappings:
            cur_value = mapping.inverse_map(cur_value)

        for (start, length) in seed_ranges:
            if cur_value in range(start, start + length):
                return location
        
        location += 1