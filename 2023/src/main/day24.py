from __future__ import annotations
import z3

def day24a(input: list[str], min_coor: int = 200000000000000, max_coor: int = 400000000000000) -> int:
    stones = parse_input(input)

    collisions: dict[tuple[int,int], tuple[float,float]] = {}
    for i in range(len(stones)):
        for j in range(i + 1, len(stones)):
            intersect = stones[i].find_intersection(stones[j])
            if intersect is not None:
                (intersect_x, intersect_y) = intersect
                intersect_time1 = (intersect_x - stones[i].x) / stones[i].vx
                intersect_time2 = (intersect_x - stones[j].x) / stones[j].vx
                if intersect_time1 >= 0 and  intersect_time2 >= 0:
                    if intersect_x >= min_coor and intersect_x <= max_coor and intersect_y >= min_coor and intersect_y <= max_coor:
                        collisions[(i,j)] = intersect
    
    return len(collisions)


def day24b(input: list[str]) -> int:
    stones = parse_input(input)

    x_start = z3.Real("x_start")
    y_start = z3.Real("y_start")
    z_start = z3.Real("z_start")
    vx = z3.Real("vx")
    vy = z3.Real("vy")
    vz = z3.Real("vz")

    solver = z3.Solver()
    for i in range(3):
        time = z3.Real(f"time{i}")
        solver.add(time > 0)
        solver.add(x_start + time * vx == stones[i].x + time * stones[i].vx)
        solver.add(y_start + time * vy == stones[i].y + time * stones[i].vy)
        solver.add(z_start + time * vz == stones[i].z + time * stones[i].vz)

    solver.check()

    return solver.model()[x_start].as_long() + solver.model()[y_start].as_long() + solver.model()[z_start].as_long()

class Stone(object):
    def __init__(self, id: int, x: int, y: int, z: int, vx: int, vy: int, vz: int):
        self.id = id
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz

    def __in_standard_form(self) -> tuple[int, int, int]:
        start = (self.x, self.y)
        end = (self.x + 10 * self.vx, self.y + 10 * self.vy)
        a = (start[1] - end[1])
        b = (start[0] - end[0])
        c = (end[0] * start[1] - start[0] * end[1])
        return a, -b, c
    
    def find_intersection(self, other: Stone) -> tuple[float, float] | None:
        (a1, b1, c1) = self.__in_standard_form()
        (a2, b2, c2) = other.__in_standard_form()
        d  = a1 * b2 - b1 * a2
        if d == 0:
            return None
        dx = c1 * b2 - b1 * c2
        dy = a1 * c2 - c1 * a2
        x = dx / d
        y = dy / d
        return (x, y)

def parse_input(input: list[str]) -> list[Stone]:
    stones: list[Stone] = []
    for id, line in enumerate(input):
        (position, velocity) = line.split(" @ ")
        (x, y, z) = map(lambda c: int(c), position.split(", "))
        (vx, vy, vz) = map(lambda v: int(v.strip()), velocity.split(", "))
        stones.append(Stone(id, x, y, z, vx, vy, vz))
    return stones