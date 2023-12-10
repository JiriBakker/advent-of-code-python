import sys

def day10a(input: list[str]) -> int:
    prev_pos = (-sys.maxsize, -sys.maxsize)
    start_pos = find_start_pos(input)
    
    cur_pos = start_pos
    path_length = 0
    while True:
        (x, y) = cur_pos
        possible_moves = find_possible_moves(input, x, y)
        # print(f"{cur_pos} {prev_pos} {path_length} {possible_moves}")
        if len(possible_moves) != 2:
            raise Exception(f"huh? {possible_moves}")

        for move in possible_moves:
            if move != prev_pos:
                prev_pos = cur_pos
                cur_pos = move
                break

        path_length += 1
        if cur_pos == start_pos:
            break

    return path_length // 2

def day10b(input: list[str]) -> int:
    grid = []
    row = []
    row2 = []
    for x in range(0, len(input[0]) * 2 + 2):
        row.append(".")
        row2.append(".")
    grid.append(row)

    for y in range(0, len(input)):
        row = ["."]
        row2 = ["."]
        for x in range(0, len(input[y]) * 2):
            row.append(".")
            row2.append(".")

        row.append(".")
        row2.append(".")
        grid.append(row)
        grid.append(row2)

    grid.append(row2)

    prev_pos = (-sys.maxsize, -sys.maxsize)
    start_pos = find_start_pos(input)
    
    cur_pos = start_pos
    while True:
        (x, y) = cur_pos
        possible_moves = find_possible_moves(input, x, y)
        # print(f"{cur_pos} {prev_pos} {path_length} {possible_moves}")
        if len(possible_moves) != 2:
            raise Exception(f"huh? {possible_moves}")

        for move in possible_moves:
            if move != prev_pos:
                prev_pos = cur_pos
                cur_pos = move

                (curx, cury) = cur_pos
                (prevx, prevy) = prev_pos

                if curx == prevx:
                    if prevy < cury:
                        grid[cury * 2 - 1 + 1][curx * 2 + 1] = "|"
                    else:
                        grid[cury * 2 + 1 + 1][curx * 2 + 1] = "|"
                else:
                    if prevx < curx:
                        grid[cury * 2 + 1][curx * 2 - 1 + 1] = "-"
                    else:
                        grid[cury * 2 + 1][curx * 2 + 1 + 1] = "-"

                grid[cury * 2 + 1][curx * 2 + 1] = input[cury][curx]
                break

        if cur_pos == start_pos:
            break

    to_visit: list[tuple[int, int]] = [(0,0)]
    # for y in range(0, len(grid)):
    #     for x in range(0, len(grid[y])):
    #         if x == 0 or x == len(grid[y]) - 1 or y == 0 or y == len(grid) - 1:
    #             to_visit.append((x, y))

    for y in range(0, len(grid)):
        print("".join(grid[y]))

    visits = 0
    seen = set()
    while len(to_visit) > 0:
        visits += 1
        (x, y) = to_visit.pop(0)
        grid[y][x] = "X"

        if x > 0 and grid[y][x - 1] == "." and (x - 1, y) not in seen:
            to_visit.append((x - 1, y))
            seen.add((x - 1, y))
        if x < len(grid[y]) - 1 and grid[y][x + 1] == "." and (x + 1, y) not in seen:
            to_visit.append((x + 1, y))
            seen.add((x + 1, y))
        if y > 0 and grid[y - 1][x] == "." and (x, y - 1) not in seen:
            to_visit.append((x, y - 1))
            seen.add((x, y - 1))
        if y < len(grid) - 1 and grid[y + 1][x] == "." and (x, y + 1) not in seen:
            to_visit.append((x, y + 1))
            seen.add((x, y + 1))


    in_loop = 0
    for y in range(1, len(grid), 2):
        for x in range(1, len(grid[y]), 2):
            print(grid[y][x], end="")
            if grid[y][x] == ".":
                in_loop += 1

        print()
        
    return in_loop

pipes_accessible_from_right = ["-", "L", "F", "S"]
pipes_accessible_from_left = ["-", "J", "7", "S"]
pipes_accessible_from_above = ["|", "L", "J", "S"]
pipes_accessible_from_below = ["|", "7", "F", "S"]

pipes_can_move_left = ["-", "J", "7", "S"]
pipes_can_move_right = ["-", "F", "L", "S"]
pipes_can_move_up = ["|", "J", "L", "S"]
pipes_can_move_down = ["|", "F", "7", "S"]

def find_start_pos(input: list[str]) -> tuple[int, int]:
    for y in range(0, len(input)):
        for x in range(0, len(input[y])):
            if input[y][x] == "S":
                return (x, y)
    raise

def find_possible_moves(input: list[str], x: int, y: int) -> list[tuple[int, int]]:
    possible_moves = []

    # left
    if (x > 0 and
        input[y][x] in pipes_can_move_left and
        input[y][x - 1] in pipes_accessible_from_right   
    ):
        possible_moves.append((x - 1, y))
    
    # right
    if (x < len(input[y]) - 1 and
        input[y][x] in pipes_can_move_right and
        input[y][x + 1] in pipes_accessible_from_left
    ):
        possible_moves.append((x + 1, y))

    # up
    if (y > 0 and
        input[y][x] in pipes_can_move_up and
        input[y - 1][x] in pipes_accessible_from_below
    ):
        possible_moves.append((x, y - 1))

    # down
    if (y < len(input) - 1 and
        input[y][x] in pipes_can_move_down and
        input[y + 1][x] in pipes_accessible_from_above
    ):
        possible_moves.append((x, y + 1))

    return possible_moves
