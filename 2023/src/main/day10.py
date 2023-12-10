def day10a(input: list[str]) -> int:
    path = trace_path(input)
    return len(path) // 2

def day10b(input: list[str]) -> int:
    path = trace_path(input)
    grid = ZoomedGrid(path, input)
    grid.flood()
    return grid.count_empty_unzoomed()

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


class ZoomedGrid(object):
    def __init__(self, path: list[tuple[int, int]], input: list[str]):
        self.height = len(input) * 2
        self.width = len(input[0]) * 2
        self.grid = {}
        self.__plot_path(path, input)
                                     
    def __plot_path(self, path: list[tuple[int, int]], input: list[str]):
        for i in range(1, len(path)):
            (prevx, prevy) = path[i - 1]
            (x, y) = path[i]

            self.__set_cell(x * 2, y * 2, input[y][x])
            if prevx == x:
                self.__set_cell(x * 2, y * 2 + (prevy - y), "|")
            else:
                self.__set_cell(x * 2 + (prevx - x), y * 2, "-")
    
    def get_cell(self, x: int, y: int) -> str:
        return self.grid[y][x] if y in self.grid and x in self.grid[y] else " "
        
    def __set_cell(self, x: int, y: int, char: str):
        self.grid[y] = self.grid.get(y, {})
        self.grid[y][x] = char
    
    def flood(self):
        to_visit: list[tuple[int, int]] = [(-1,-1)]
        while len(to_visit) > 0:
            (x, y) = to_visit.pop(0)
            self.__set_cell(x, y, "X")

            if x >= 0 and self.get_cell(x - 1, y) == " " and (x - 1, y) not in to_visit:
                to_visit.append((x - 1, y))
            if x < self.width and self.get_cell(x + 1, y) == " " and (x + 1, y) not in to_visit:
                to_visit.append((x + 1, y))
            if y >= 0 and self.get_cell(x, y - 1) == " " and (x, y - 1) not in to_visit:
                to_visit.append((x, y - 1))
            if y < self.height and self.get_cell(x, y + 1) == " " and (x, y + 1) not in to_visit:
                to_visit.append((x, y + 1))

    def count_empty_unzoomed(self) -> int:
        empty_count = 0
        for y in range(0, self.height, 2):
            for x in range(0, self.width, 2):
                if self.get_cell(x, y) == " ":
                    empty_count += 1
        return empty_count