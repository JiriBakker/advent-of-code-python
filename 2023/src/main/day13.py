def day13a(input: list[str]) -> int:
    patterns = parse_patterns(input)
    total = 0
    for pattern in patterns:
        x_split = find_vertical_split(pattern)
        y_split = find_horizontal_split(pattern)
        total += x_split + 100 * y_split
    return total

def day13b(input: list[str]) -> int:
    patterns = parse_patterns(input)
    total = 0
    initial_splits = []
    for pattern in patterns:
        x_split = find_vertical_split(pattern)
        y_split = find_horizontal_split(pattern)
        initial_splits.append((pattern, x_split, y_split))

    for (pattern, x_split, y_split) in initial_splits:
        x_split2 = find_vertical_split(pattern, x_split)
        y_split2 = find_horizontal_split(pattern, y_split)
        total += x_split2 + 100 * y_split2
    return total

def parse_patterns(input: list[str]) -> list[list[str]]:
    patterns = [[]]
    for line in input:
        if len(line) == 0:
            patterns.append([])
        else:
            patterns[-1].append(line)
    return patterns
    
def find_vertical_split(pattern: list[str], ignore_x: int | None = None) -> int:
    for x in range(1, len(pattern[0])):
        if x == ignore_x:
            continue
        if is_mirrored_horizontally(pattern, x, allow_smudge = ignore_x is not None):
            return x
    return 0

def is_mirrored_horizontally(pattern: list[str], split_x: int, allow_smudge: bool) -> bool:
    smudge: tuple[int, int] | None = None
    for y in range(0, len(pattern)):
        x_delta_max = min(len(pattern[y]) - split_x, split_x)
        for x_delta in range(0, x_delta_max):
            if pattern[y][split_x - x_delta - 1] != pattern[y][split_x + x_delta]:
                if allow_smudge and smudge is None:
                    smudge = (split_x - x_delta - 1, y)
                else:
                    return False
    return True

def find_horizontal_split(pattern: list[str], ignore_y: int | None = None) -> int:
    for y in range(1, len(pattern)):
        if y == ignore_y:
            continue
        if is_mirrored_vertically(pattern, y, allow_smudge = ignore_y is not None):
            return y
    return 0

def is_mirrored_vertically(pattern: list[str], split_y: int, allow_smudge: bool) -> bool:
    smudge: tuple[int, int] | None = None
    y_delta_max = min(len(pattern) - split_y, split_y)
    for y_delta in range(0, y_delta_max):
        for x in range(0, len(pattern[0])):
            if pattern[split_y - y_delta - 1][x] != pattern[split_y + y_delta][x]:
                if allow_smudge and smudge is None:
                    smudge = (x, split_y - y_delta - 1)
                else:
                    return False
    return True