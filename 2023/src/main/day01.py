from main.util import min_by, max_by

def day01a(input: list[str]) -> int:
    numberSet = {  "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9 }
    return compute_calibration_value(input, numberSet)

def day01b(input: list[str]) -> int:
    numberSet = { "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9 }
    return compute_calibration_value(input, numberSet)

def compute_calibration_value(lines: list[str], numberSet: dict[str, int]) -> int:
    def get_number(line: str) -> int:
        def filter_not_found(occurrences: dict[str, int]) -> list[tuple[str, int]]:
            return list(filter(lambda occurrence: occurrence[1] != -1, occurrences.items()))
            
        (firstNr, _) = min_by(lambda x: x[1], filter_not_found(dict(map(lambda nr: (nr, line.find(nr)), numberSet.keys()))))
        (lastNr, _)  = max_by(lambda x: x[1], filter_not_found(dict(map(lambda nr: (nr, line.rfind(nr)), numberSet.keys()))))

        return int(f"{numberSet[firstNr]}{numberSet[lastNr]}")
    
    return sum(map(lambda line: get_number(line), lines))