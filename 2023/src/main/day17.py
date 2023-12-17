from dataclasses import dataclass, field
from enum import Enum
from queue import PriorityQueue
from typing import Any
from main.util import is_within_bounds

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

@dataclass(order=True)
class Step(object):
    cost: int
    x: int = field(compare = False)
    y: int = field(compare = False)
    direction: Direction = field(compare = False)
    straight_steps: int
    prev: Any | None = field(compare = False)

def day17a(input: list[str]) -> int:
    return find_min_heat_cost(input, max_straight_steps = 3)

def day17b(input: list[str]) -> int:
    return find_min_heat_cost(input, max_straight_steps = 10, min_straight_steps = 4)

def find_min_heat_cost(input: list[str], max_straight_steps: int, min_straight_steps: int = 0) -> int:
    target_pos = (len(input[0]) - 1, len(input) - 1)

    to_visit = PriorityQueue[Step]()
    to_visit.put(Step(0, 0, 0, Direction.RIGHT, 0, prev = None))

    visited: set[tuple[int, int, int, Direction]] = set()
    while not to_visit.empty():
        step = to_visit.get()

        if (step.x, step.y, step.straight_steps, step.direction) in visited:
            continue
        visited.add((step.x, step.y, step.straight_steps, step.direction))

        if (step.x, step.y) == target_pos:
            return step.cost
 
        next_directions: list[Direction] = []
        if step.direction == Direction.RIGHT:
            if step.straight_steps < max_straight_steps:
                next_directions.append(Direction.RIGHT)
            if step.straight_steps >= min_straight_steps:
                next_directions.append(Direction.UP)
                next_directions.append(Direction.DOWN)
        if step.direction == Direction.LEFT:
            if step.straight_steps < max_straight_steps:
                next_directions.append(Direction.LEFT)
            if step.straight_steps >= min_straight_steps:
                next_directions.append(Direction.UP)
                next_directions.append(Direction.DOWN)
        if step.direction == Direction.UP:
            if step.straight_steps < max_straight_steps:
                next_directions.append(Direction.UP)
            if step.straight_steps >= min_straight_steps:
                next_directions.append(Direction.LEFT)
                next_directions.append(Direction.RIGHT)
        if step.direction == Direction.DOWN:
            if step.straight_steps < max_straight_steps:
                next_directions.append(Direction.DOWN)
            if step.straight_steps >= min_straight_steps:
                next_directions.append(Direction.LEFT)
                next_directions.append(Direction.RIGHT)

        for next_direction in next_directions:
            next_x = step.x
            next_y = step.y
            if next_direction == Direction.UP:    next_y -= 1
            if next_direction == Direction.DOWN:  next_y += 1
            if next_direction == Direction.LEFT:  next_x -= 1
            if next_direction == Direction.RIGHT: next_x += 1

            if not is_within_bounds(next_x, next_y, input):
                continue
            
            next_straight_steps = step.straight_steps + 1 if next_direction == step.direction else 1
            next_cost = step.cost + int(input[next_y][next_x])

            to_visit.put(Step(next_cost, next_x, next_y, next_direction, next_straight_steps, prev = step))

    raise Exception("No path found")