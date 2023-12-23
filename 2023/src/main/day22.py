from __future__ import annotations
from main.util import all, count

def day22a(input: list[str]) -> int:
    bricks = parse_input(input)
    
    bricks.sort(key = lambda brick: brick.zlow)

    for brick in bricks:
        brick.move_down_until_blocked(bricks)

    supporting_brick_ids: set[int] = set()
    for brick in bricks:
        if len(brick.supported_by) == 1:
            supporting_brick_ids.add(brick.supported_by[0].id)

    return len(input) - len(supporting_brick_ids)

def day22b(input: list[str]) -> int:
    bricks = parse_input(input)
    
    bricks.sort(key = lambda brick: brick.zlow)

    for brick in bricks:
        brick.move_down_until_blocked(bricks)

    affected_brick_count = 0
    for disintegrated_brick in bricks:
        stable_brick_ids: set[int] = set()
        potentially_affected_bricks: set[Brick] = set()

        # Find which bricks are supported directly or indirectly by the disintegrated brick
        bricks_to_check: list[Brick] = [disintegrated_brick]
        while len(bricks_to_check) > 0:
            brick = bricks_to_check.pop(0)
            potentially_affected_bricks.add(brick)
            for supported_brick in brick.supports:
                bricks_to_check.append(supported_brick)

        # For each potentially affected brick, see if there is any 'parent' brick that is supported by the floor
        for potentially_affected_brick in potentially_affected_bricks:
            bricks_below: list[Brick] = [potentially_affected_brick]

            while len(bricks_below) > 0:
                brick_below = bricks_below.pop(0)
                if brick_below.id == disintegrated_brick.id:
                    continue

                if all(lambda b: b.id in stable_brick_ids and b.id != disintegrated_brick.id, brick_below.supported_by):
                    stable_brick_ids.add(potentially_affected_brick.id)
                    stable_brick_ids.add(brick_below.id)
                    bricks_below = []
                    continue

                for supporting_brick in brick_below.supported_by:
                    bricks_below.append(supporting_brick)

        affected_brick_count += count(lambda b: b.id not in stable_brick_ids and b.id != disintegrated_brick.id, potentially_affected_bricks)

    return affected_brick_count

class Brick(object):
    def __init__(self, id: int, x1: int, y1: int, z1: int, x2: int, y2: int, z2: int):
        self.id = id
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1
        self.x2 = x2
        self.y2 = y2
        self.z2 = z2
        self.zlow = min(z1, z2)
        self.supported_by: list[Brick] = []
        self.supports: list[Brick] = []

    def move_down_until_blocked(self, others: list[Brick]):
        while True:
            if self.zlow == 1:
                return
            
            for other in others:
                if self == other:
                    continue
                if has_overlap(self.x1, self.x2, other.x1, other.x2) and has_overlap(self.y1, self.y2, other.y1, other.y2) and has_overlap(self.z1 - 1, self.z2 - 1, other.z1, other.z2):
                    self.supported_by.append(other)
                    other.supports.append(self)

            if len(self.supported_by) > 0:
                return

            self.zlow -= 1
            self.z1 -= 1
            self.z2 -= 1

    def __str__(self) -> str:
        return f"[{self.id}] ({self.x1},{self.y1},{self.zlow})-({self.x2},{self.y2},{self.z2})"
    
def has_overlap(start1: int, end1: int, start2: int, end2: int) -> bool:
    return start1 <= end2 and end1 >= start2

def parse_input(input: list[str]) -> list[Brick]:
    bricks: list[Brick] = []
    id = 1
    for line in input:
        (start, end) = line.split("~")
        (x1, y1, z1) = start.split(",")
        (x2, y2, z2) = end.split(",")
        bricks.append(Brick(id, int(x1), int(y1), int(z1), int(x2), int(y2), int(z2)))
        id += 1
    return bricks