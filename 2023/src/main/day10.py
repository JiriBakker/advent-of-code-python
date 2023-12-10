def day10a(input: list[str]) -> int:
    path = trace_path(input)
    return len(path) // 2

def day10b(input: list[str]) -> int:
    width = len(input[0])
    height = len(input)

    path = trace_path(input)
    grid = plot_on_zoomed_grid(path, input)
    filled_grid = fill_grid(grid, width * 2, height * 2)

    return count_empty_unzoomed(filled_grid, width * 2, height * 2)


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

def trace_path(input: list[str]) -> list[tuple[int, int]]:
    start_pos = find_start_pos(input)
    cur_pos = start_pos
    
    path = [start_pos]
    while True:
        (x, y) = cur_pos
        
        for move in find_possible_moves(input, x, y):
            if len(path) < 2 or move != path[-2]:
                path.append(move)
                cur_pos = move
                break

        if cur_pos == start_pos:
            break

    return path

def find_possible_moves(input: list[str], x: int, y: int) -> list[tuple[int, int]]:
    possible_moves = []

    if (x > 0 and
        input[y][x] in pipes_can_move_left and
        input[y][x - 1] in pipes_accessible_from_right   
    ):
        possible_moves.append((x - 1, y))
    
    if (x < len(input[y]) - 1 and
        input[y][x] in pipes_can_move_right and
        input[y][x + 1] in pipes_accessible_from_left
    ):
        possible_moves.append((x + 1, y))

    if (y > 0 and
        input[y][x] in pipes_can_move_up and
        input[y - 1][x] in pipes_accessible_from_below
    ):
        possible_moves.append((x, y - 1))

    if (y < len(input) - 1 and
        input[y][x] in pipes_can_move_down and
        input[y + 1][x] in pipes_accessible_from_above
    ):
        possible_moves.append((x, y + 1))

    return possible_moves

def plot_on_zoomed_grid(path: list[tuple[int, int]], input: list[str]) -> dict[int, dict[int, str]]:
    grid = {}
    def set_cell(x: int, y: int, char: str):
        grid[y] = grid.get(y, {})
        grid[y][x] = char

    for i in range(1, len(path)):
        (prevx, prevy) = path[i - 1]
        (x, y) = path[i]

        set_cell(x * 2, y * 2, input[y][x])
        if prevx == x:
            set_cell(x * 2, y * 2 + (prevy - y), "|")
        else:
            set_cell(x * 2 + (prevx - x), y * 2, "-")
    
    return grid

def fill_grid(grid: dict[int, dict[int, str]], width: int, height: int) -> dict[int, dict[int, str]]:
    to_visit: list[tuple[int, int]] = [(-1,-1)]

    def get_cell(x: int, y: int) -> str:
        return grid[y][x] if y in grid and x in grid[y] else " "
    
    def set_cell(x: int, y: int, char: str):
        grid[y] = grid.get(y, {})
        grid[y][x] = char

    while len(to_visit) > 0:
        (x, y) = to_visit.pop(0)
        set_cell(x, y, "X")

        if x >= 0 and get_cell(x - 1, y) == " " and (x - 1, y) not in to_visit:
            to_visit.append((x - 1, y))
        if x < width and get_cell(x + 1, y) == " " and (x + 1, y) not in to_visit:
            to_visit.append((x + 1, y))
        if y >= 0 and get_cell(x, y - 1) == " " and (x, y - 1) not in to_visit:
            to_visit.append((x, y - 1))
        if y < height and get_cell(x, y + 1) == " " and (x, y + 1) not in to_visit:
            to_visit.append((x, y + 1))

    return grid

def count_empty_unzoomed(grid: dict[int, dict[int, str]], width: int, height: int) -> int:
    empty_count = 0
    for y in range(0, height, 2):
        for x in range(0, width, 2):
            if y not in grid or x not in grid[y] or grid[y][x] == " ":
                empty_count += 1
    return empty_count