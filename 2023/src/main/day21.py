
def day21a(input: list[str], nr_of_steps: int = 64) -> int:
    ((start_x, start_y), blocked_positions) = parse_input(input)

    visited: dict[tuple[int,int], int] = {}
    will_visit: set[tuple[int,int]] = set()

    to_visit: list[tuple[int,int,int]] = [(start_x, start_y, 0)]
    def add_to_visit(x: int, y: int, steps: int):
        if steps <= nr_of_steps and (x, y) not in will_visit:
            to_visit.append((x, y, steps))
            will_visit.add((x, y))

    while len(to_visit) > 0:
        (x, y, steps) = to_visit.pop(0)

        if y in blocked_positions and x in blocked_positions[y]:
            continue

        if (x, y) not in visited:
            visited[(x, y)] = steps

        add_to_visit(x + 1, y, steps + 1)
        add_to_visit(x - 1, y, steps + 1)
        add_to_visit(x, y + 1, steps + 1)
        add_to_visit(x, y - 1, steps + 1)

    reachable = list(filter(lambda steps: (steps + 2) % 2 == 0, visited.values()))


    return len(reachable)



def day21b(input: list[str]) -> int:
    # key values found after analyzing grid progression
    first_key_step_count = 65
    second_key_step_count = 327
    final_key_step_count = 589

    ((start_x, start_y), blocked_positions) = parse_input(input)

    width = len(input[0])
    height = len(input) 

    visited: dict[tuple[int,int], int] = {}
    will_visit: set[tuple[int,int]] = set()
    reachable_count = 0

    to_visit: list[tuple[int,int,int]] = [(start_x, start_y, 0)]
    def add_to_visit(x: int, y: int, steps: int):
        if (x, y) not in will_visit:
            to_visit.append((x, y, steps))
            will_visit.add((x, y))

    first_key_step_count_reachable_count = 0
    second_key_step_count_reachable_count = 0
    while len(to_visit) > 0:
        (x, y, steps) = to_visit.pop(0)

        if steps == first_key_step_count + 1 and first_key_step_count_reachable_count == 0:
            first_key_step_count_reachable_count = reachable_count

        if steps == second_key_step_count + 1 and second_key_step_count_reachable_count == 0:
            second_key_step_count_reachable_count = reachable_count

        if steps == final_key_step_count + 1:
            return extrapolate_reachable_count(first_key_step_count_reachable_count, second_key_step_count_reachable_count, reachable_count)
           
        if ((y + height) % height) in blocked_positions and ((x + width) % width) in blocked_positions[(y + height) % height]:
            continue

        if (x, y) not in visited:
            visited[(x, y)] = steps
            if (steps + 2) % 2 == 1:
                reachable_count += 1

        add_to_visit(x + 1, y, steps + 1)
        add_to_visit(x - 1, y, steps + 1)
        add_to_visit(x, y + 1, steps + 1)
        add_to_visit(x, y - 1, steps + 1)

    return reachable_count

# The reachable positions increase quadratically in a cycle of 262 steps, so we can use that to extrapolate the reachable count at step 26501365
def extrapolate_reachable_count(first_key_step_count_reachable_count: int, second_key_step_count_reachable_count: int, third_key_step_count_reachable_count: int) -> int:
    delta1 = second_key_step_count_reachable_count - first_key_step_count_reachable_count
    delta2 = third_key_step_count_reachable_count - second_key_step_count_reachable_count
    delta_delta = delta2 - delta1

    cycles_remaining = int((26501365 - 589) / 262)

    delta_base = delta2 * cycles_remaining
    delta_sum = int(cycles_remaining * (cycles_remaining + 1) / 2) * delta_delta + delta_base

    return third_key_step_count_reachable_count + delta_sum

def parse_input(input: list[str]) -> tuple[tuple[int,int],dict[int,set[int]]]:
    grid: dict[int,set[int]] = {}
    start_pos = None
    for y in range(0, len(input)):
        for x in range(0, len(input[0])):
            if input[y][x] == "#":
                if y not in grid:
                    grid[y] = set()
                grid[y].add(x)
            elif input[y][x] == "S":
                start_pos = (x, y)

    if start_pos == None:
        raise

    return (start_pos, grid)