
import random
import heapq





# -----------------------
# Constants / Tile types
# -----------------------
ROCK = '#'
TREE = 'T'
WATER = '~'
EMPTY = '.'
MED_DEPOT = 'M'
AMMO_DEPOT = 'A'

TILE_PASSABLE = {
    ROCK: False,
    WATER: False,
    TREE: True,
    EMPTY: True,
    MED_DEPOT: True,
    AMMO_DEPOT: True,
}

TILE_BLOCKS_VISION = {
    ROCK: True,
    TREE: True,
    WATER: False,
    EMPTY: False,
    MED_DEPOT: False,
    AMMO_DEPOT: False,
}

# -----------------------
# Utility functions
# -----------------------

def neighbors(pos, w, h):
    x, y = pos
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < w and 0 <= ny < h:
            yield (nx, ny)


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def bresenham_line(a, b):
    # returns list of integer points between a (inclusive) and b (inclusive)
    x0, y0 = a
    x1, y1 = b
    points = []
    dx = abs(x1 - x0)
    dy = -abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx + dy
    while True:
        points.append((x0, y0))
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 >= dy:
            err += dy
            x0 += sx
        if e2 <= dx:
            err += dx
            y0 += sy
    return points

# -----------------------
# MapGrid
# -----------------------
class MapGrid:
    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        # grid[x][y] layout (width-major) — this is consistent across code
        self.grid = [[EMPTY for _ in range(height)] for _ in range(width)]
        self._place_random_obstacles()

    def _place_random_obstacles(self):
        # For demo: scatter some rocks, trees, water, and depots
        for x in range(self.w):
            for y in range(self.h):
                r = random.random()
                if r < 0.06:
                    self.grid[x][y] = ROCK
                elif r < 0.14:
                    self.grid[x][y] = TREE
                elif r < 0.18:
                    self.grid[x][y] = WATER
                # else empty
        # place depots
        for _ in range(2):
            self._place_tile_random(MED_DEPOT)
            self._place_tile_random(AMMO_DEPOT)

    def _place_tile_random(self, tile):
        for _ in range(200):
            x = random.randrange(self.w)
            y = random.randrange(self.h)
            if self.grid[x][y] == EMPTY:
                self.grid[x][y] = tile
                return