from main.util import filter_empty

def day04a(input: list[str]) -> int:
    scratchcard_matches = filter_empty(find_scratchcards_matches(input))
    return sum(map(lambda matches: 2 ** (len(matches) - 1), scratchcard_matches))

def day04b(input: list[str]) -> int:
    scratchcard_matches = find_scratchcards_matches(input)
    return stack_points(scratchcard_matches)
    
def find_scratchcards_matches(input: list[str]):
    def parse_scratchcard(line: str) -> tuple[list[int], list[int]]:
        winning_numbers = list(map(lambda nr: int(nr), filter_empty(line.split(":")[1].split("|")[0].strip().split(" "))))
        my_numbers = list(map(lambda nr: int(nr), filter_empty(line.split("|")[1].strip().split(" "))))
        return (winning_numbers, my_numbers)
    
    def find_matches(line: str) -> list[int]:
        (winning_numbers, my_numbers) = parse_scratchcard(line)
        return list(filter(lambda nr: nr in my_numbers, winning_numbers))

    return list(map(lambda line: find_matches(line), input))

def stack_points(scratchcard_matches: list[list[int]]) -> int:
    match_counts = list(map(lambda scratchcard: len(scratchcard), scratchcard_matches))

    stacked_counts: dict[int, int] = {}
    for i in range(len(match_counts) - 1, -1, -1):
        stacked_counts[i] = 1
        for j in range(i + 1, min(i + match_counts[i] + 1, len(match_counts))):
            stacked_counts[i] += stacked_counts[j]

    return sum(stacked_counts.values())
