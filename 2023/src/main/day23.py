from __future__ import annotations
from dataclasses import dataclass
from main.util import first_or_none

def day23a(input: list[str]) -> int:
    x_target = len(input[0]) - 2
    y_target = len(input) - 1

    def is_within_bounds(x: int, y: int, input: list[str]) -> bool:
        return x >= 0 and x < len(input[0]) and y >= 0 and y < len(input)

    to_visit: list[tuple[int, int, int, list[tuple[int, int]]]] = [(1, 0, 0, [])]

    max_distance = 0
    while len(to_visit) > 0:
        (x, y, distance, prev_visited) = to_visit.pop(0)
        if (x, y) in prev_visited:
            continue

        visited = prev_visited.copy()
        visited.append((x, y))

        def add_to_visited(x: int, y: int):
            if is_within_bounds(x, y, input) and input[y][x] != "#" and (x, y) not in visited:
                to_visit.append((x, y, distance + 1, visited))


        if x == x_target and y == y_target:
            max_distance = max(max_distance, distance)
            continue
        
        if input[y][x] == ">":
            to_visit.append((x + 1, y, distance + 1, visited))
        elif input[y][x] == "<":
            to_visit.append((x - 1, y, distance + 1, visited))
        elif input[y][x] == "^":
            to_visit.append((x, y - 1, distance + 1, visited))
        elif input[y][x] == "v":
            to_visit.append((x, y + 1, distance + 1, visited))
        else:
            add_to_visited(x + 1, y)
            add_to_visited(x - 1, y)
            add_to_visited(x, y + 1)
            add_to_visited(x, y - 1)

    return max_distance

@dataclass
class Node(object):
    x: int
    y: int
    neighbours: dict[tuple[int, int], int]

    def __hash__(self) -> int:
        return self.y * 1_000_000 + self.x

def day23b(input: list[str]) -> int:
    x_target = len(input[0]) - 2
    y_target = len(input) - 1

    def is_within_bounds(x: int, y: int, input: list[str]) -> bool:
        return x >= 0 and x < len(input[0]) and y >= 0 and y < len(input) and input[y][x] != "#"
    
    visited: set[tuple[int, int]] = set()
    def find_next_intersection(x: int, y: int, distance: int) -> tuple[int, int, int] | None:
        if (x, y) in visited:
            return None

        if x == x_target and y == y_target:
            return (x, y, distance)

        neighbours: dict[tuple[int,int], str] = {}
        if is_within_bounds(x + 1, y, input):
            neighbours[(x + 1, y)] = input[y][x + 1]
        if is_within_bounds(x - 1, y, input):
            neighbours[(x - 1, y)] = input[y][x - 1]
        if is_within_bounds(x, y + 1, input):
            neighbours[(x, y + 1)] = input[y + 1][x]
        if is_within_bounds(x, y - 1, input):
            neighbours[(x, y - 1)] = input[y - 1][x]

        open_neighbours = dict(filter(lambda n: n[1] != "#", neighbours.items()))

        if len(open_neighbours) == 1:
            return None
        
        if len(open_neighbours) == 2:
            next_neighbour = first_or_none(lambda n: n[0] not in visited, open_neighbours.items())
            if next_neighbour is None:
                return None
            visited.add((x, y))
            return find_next_intersection(next_neighbour[0][0], next_neighbour[0][1], distance + 1)
        
        return (x, y, distance)
    
    start = Node(1, 0, {})
    nodes: dict[tuple[int, int], Node] = {(1, 0): start}
    to_visit: list[tuple[int, int, Node]] = [(1, 0, start)]

    while len(to_visit) > 0:
        (x, y, prev) = to_visit.pop(0)
        if (x, y) in visited:
            continue

        visited.add((x, y))

        if x == x_target and y == y_target:
            continue

        intersections: list[tuple[int, int, int]] = []
        if is_within_bounds(x + 1, y, input):
            intersection = find_next_intersection(x + 1, y, 1)
            if intersection is not None:
                intersections.append(intersection)
                
        if is_within_bounds(x - 1, y, input):
            intersection = find_next_intersection(x - 1, y, 1)
            if intersection is not None:
                intersections.append(intersection)
        if is_within_bounds(x, y + 1, input):
            intersection = find_next_intersection(x, y + 1, 1)
            if intersection is not None:
                intersections.append(intersection)
        if is_within_bounds(x, y - 1, input):
            intersection = find_next_intersection(x, y - 1, 1)
            if intersection is not None:
                intersections.append(intersection)
        
        for intersection in intersections:
            (x_intersect, y_intersect, distance) = intersection
            node = nodes.get((x_intersect, y_intersect), Node(x_intersect, y_intersect, {}))
            node.neighbours[(prev.x, prev.y)] = distance
            prev.neighbours[(node.x, node.y)] = distance
            nodes[(x_intersect, y_intersect)] = node
            to_visit.append((x_intersect, y_intersect, node))

    nodes_to_visit: list[tuple[Node, int, set[tuple[int, int]]]] = [(start, 0, set())]
    max_distance = 0

    while len(nodes_to_visit) > 0:
        (node, distance, prev_visited) = nodes_to_visit.pop()

        if (node.x, node.y) in prev_visited:
            continue

        if node.x == x_target and node.y == y_target:
            if distance > max_distance:
                max_distance = max(max_distance, distance)
            continue

        for neighbour in node.neighbours:
            if neighbour in prev_visited:
                continue
            nodes_to_visit.append((nodes[neighbour], distance + node.neighbours[neighbour], prev_visited | {(node.x, node.y)}))

    return max_distance