import sys
from main.util import none, manhattan_distance

def day11a(input: list[str]) -> int:
    galaxy_map = parse_map(input)
    galaxy_map.expand(delta = 1)
    return galaxy_map.sum_distances()

def day11b(input: list[str], delta: int = 1_000_000) -> int:
    galaxy_map = parse_map(input)
    galaxy_map.expand(delta = delta - 1)
    return galaxy_map.sum_distances()

class GalaxyMap(object):
    def __init__(self):
        self.galaxies = []
        self.min_x = sys.maxsize
        self.max_x = -sys.maxsize
        self.min_y = sys.maxsize
        self.max_y = -sys.maxsize

    def add_galaxy(self, x: int, y: int):
        self.galaxies.append((x, y))
        self.min_x = min(self.min_x, x)
        self.max_x = max(self.max_x, x)
        self.min_y = min(self.min_y, y)
        self.max_y = max(self.max_y, y)

    def __move_right(self, x_divider: int, delta: int):
        updated_galaxies = []
        for (x, y) in self.galaxies:
            if x > x_divider:
                updated_galaxies.append((x + delta, y))
            else:
                updated_galaxies.append((x, y))
        self.galaxies = updated_galaxies
        self.max_x += delta

    def __move_down(self, y_divider: int, delta: int):
        updated_galaxies = []
        for (x, y) in self.galaxies:
            if y > y_divider:
                updated_galaxies.append((x, y + delta))
            else:
                updated_galaxies.append((x, y))
        self.galaxies = updated_galaxies
        self.max_y += delta

    def expand(self, delta: int):
        x_moves = []
        for x in range(self.min_x, self.max_x):
            if none(lambda galaxy: galaxy[0] == x, self.galaxies):
                x_moves.append(x)
        for x in sorted(x_moves, reverse=True):
            self.__move_right(x, delta)

        y_moves = []
        for y in range(self.min_y + 1, self.max_y):
            if none(lambda galaxy: galaxy[1] == y, self.galaxies):
                y_moves.append(y)
        for y in sorted(y_moves, reverse=True):
            self.__move_down(y, delta)

    def sum_distances(self):
        sum_distance = 0
        for i in range(0, len(self.galaxies)):
            (x1, y1) = self.galaxies[i]
            for j in range(i + 1, len(self.galaxies)):
                (x2, y2) = self.galaxies[j]
                sum_distance += manhattan_distance(x1, y1, x2, y2)
        return sum_distance
    
def parse_map(input: list[str]) -> GalaxyMap:
    galaxy_map = GalaxyMap()
    for y in range(0, len(input)):
        for x in range(0, len(input[y])):
            if input[y][x] == "#":
                galaxy_map.add_galaxy(x, y)

    return galaxy_map