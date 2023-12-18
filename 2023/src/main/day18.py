def day18a(input: list[str]) -> int:
    dig_plan = parse_dig_plan(input)
    return get_count_after_dig_plan(dig_plan)

def day18b(input: list[str]) -> int:
    dig_plan = parse_dig_plan(input)

    converted_dig_plan: list[tuple[str, int, str]] = []
    for (_, _, color) in dig_plan:
        distance2 = int(color[:5], 16)
        
        if   color[-1] == "0": direction2 = "R"
        elif color[-1] == "1": direction2 = "D"
        elif color[-1] == "2": direction2 = "L"
        else:                  direction2 = "U"

        converted_dig_plan.append((direction2, distance2, color))
    
    return get_count_after_dig_plan(converted_dig_plan)

def get_count_after_dig_plan(dig_plan: list[tuple[str, int, str]]) -> int:
    grid: dict[int, dict[int, bool]] = {}
    def add_to_grid(x: int, y: int, is_edge: bool):
        if y not in grid:
            grid[y] = {}
        if x not in grid[y] or not is_edge:
            grid[y][x] = is_edge

    x = 0
    y = 0

    for (direction, distance, _) in dig_plan:
        for _ in range(0, distance):
            add_to_grid(x, y, False)
            if direction == "R": 
                add_to_grid(x, y - 1, True)
                x += 1
                add_to_grid(x, y - 1, True)
            elif direction == "L": 
                add_to_grid(x, y + 1, True)
                x -= 1
                add_to_grid(x, y + 1, True)
            elif direction == "U": 
                add_to_grid(x - 1, y, True)
                y -= 1
                add_to_grid(x - 1, y, True)
            elif direction == "D": 
                add_to_grid(x + 1, y, True)
                y += 1
                add_to_grid(x + 1, y, True)

    count = 0
    for (y, row) in grid.items():
        range_start_x: int | None = None
        sorted_row = sorted(row.items(), key=lambda cell: cell[0])   
        for (x, is_edge) in sorted_row:
            if is_edge:
                if range_start_x != None:
                    count += (x - range_start_x)
                    range_start_x = None
                continue
            elif range_start_x == None:
                range_start_x = x

    return count

def parse_dig_plan(input: list[str]) -> list[tuple[str, int, str]]:
    dig_plan: list[tuple[str, int, str]] = []
    for line in input:
        (direction, distance, color) = line.split(" ")
        dig_plan.append((direction, int(distance), color.rstrip(")").lstrip("(#")))
    return dig_plan