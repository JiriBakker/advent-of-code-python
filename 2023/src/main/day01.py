from functools import reduce

def day01a(input: list[str]) -> int:
    numberSet = {  "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9 }
    return sum(map(lambda line: compute_calibration_value(line, numberSet), input))

def day01b(input: list[str]) -> int:
    numberSet = { "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9 }
    return sum(map(lambda line: compute_calibration_value(line, numberSet), input))

def compute_calibration_value(line: str, numberSet: dict[str, int]) -> int:
    def filter_not_found(occurrences: dict[str, int]) -> dict[str, int]:
        return dict(filter(lambda occurrence: occurrence[1] != -1, occurrences.items()))
        
    def find_min(occurrences: dict[str, int]) -> tuple[str, int]:
        return reduce(lambda minFound, occurrence: minFound if minFound[1] < occurrence[1] else occurrence, occurrences.items())
    
    def find_max(occurrences: dict[str, int]) -> tuple[str, int]:
        return reduce(lambda maxFound, occurrence: maxFound if maxFound[1] > occurrence[1] else occurrence, occurrences.items())

    (firstNr, _) = find_min(filter_not_found(dict(map(lambda nr: (nr, line.find(nr)), numberSet.keys()))))
    (lastNr, _) = find_max(filter_not_found(dict(map(lambda nr: (nr, line.rfind(nr)), numberSet.keys()))))

    return int(f"{numberSet[firstNr]}{numberSet[lastNr]}")