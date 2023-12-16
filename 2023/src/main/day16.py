from main.util import max_of

def day16a(input: list[str]) -> int:
    return energize(0, 0, 1, 0, input)

def day16b(input: list[str]) -> int:
    return max([
        max_of(lambda y: energize(0, y, 1, 0, input), range(0, len(input))),
        max_of(lambda y: energize(len(input[0]) - 1, y, -1, 0, input), range(0, len(input))),
        max_of(lambda x: energize(x, 0, 0, 1, input), range(0, len(input[0]))),
        max_of(lambda x: energize(x, len(input) - 1, 0, -1, input), range(0, len(input[0])))
    ])

def energize(start_x: int, start_y: int, start_dx: int, start_dy: int, input: list[str]):
    grid = list(map(lambda line: list(map(lambda char: (char, set()), line)), input))

    to_visit = [(start_x, start_y, start_dx, start_dy)]

    while len(to_visit) > 0:
        (x, y, dx, dy) = to_visit.pop()

        if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
            continue

        (char, visited) = grid[y][x]
        if dx == 1:
            if ">" in visited: continue
            else: visited.add(">")
        if dx == -1:
            if "<" in visited: continue
            else: visited.add("<")
        if dy == 1:
            if "v" in visited: continue
            else: visited.add("v")
        if dy == -1:
            if "^" in visited: continue
            else: visited.add("^")

        def go_left():  to_visit.append((x - 1, y, -1, 0))
        def go_right(): to_visit.append((x + 1, y, 1, 0))
        def go_up():    to_visit.append((x, y - 1, 0, -1))
        def go_down():  to_visit.append((x, y + 1, 0, 1))

        if char == "|" and dx != 0:
            go_up()
            go_down()
        elif char == "-" and dy != 0:
            go_left()
            go_right()
        elif char == "/":
            if dx == 1:    go_up()
            elif dx == -1: go_down()
            elif dy == 1:  go_left()
            else:          go_right()
        elif char == "\\":
            if dx == 1:    go_down()
            elif dx == -1: go_up()
            elif dy == 1:  go_right()
            else:          go_left()
        else:
            to_visit.append((x + dx, y + dy, dx, dy))

    return count_energized(grid)

def count_energized(grid: list[list[tuple[str, set]]]) -> int:
    energized_count = 0
    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            (_, visited) = grid[y][x]
            if len(visited) > 0:
                energized_count += 1
    
    return energized_count