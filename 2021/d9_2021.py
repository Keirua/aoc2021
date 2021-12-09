import aoc
import pprint
from collections import deque
from math import prod
pp = pprint.PrettyPrinter(indent=4)

input = aoc.input_as_string(aoc.challenge_filename(9, 2021))
test_input = """2199943210
3987894921
9856789892
8767896789
9899965678"""


class Grid:
    def __init__(self):
        self.lines = []

    def set(self, x, y, v):
        self.lines[y][x] = v

    def get(self, x, y):
        return self.lines[y][x]

    def all_coords(self):
        for x in range(self.w):
            for y in range(self.h):
                yield x, y

    def __str__(self):
        """Display these values as a 2-D grid.
        Inspired by norvig’s sudoku: http://norvig.com/sudoku.html
        """
        width = 1 + max([len(str(self.lines[y][x])) for (x, y) in self.all_coords()])
        line = ""
        for l in self.lines:
            line += ''.join([str(c).center(width) for c in l]) + "\n"
        return line


class HeightMapGrid(Grid):
    def __init__(self, lines):
        self.lines = [list(map(lambda c: int(c), line)) for line in lines]
        self.w = len(self.lines[0])
        self.h = len(self.lines)

    def is_in_grid(self, x, y) -> bool:
        return 0 <= x < self.w and 0 <= y < self.h

    def neighbours4(self, x, y):
        offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        return [(x + dx, y + dy) for (dx, dy) in offsets if self.is_in_grid(x + dx, y + dy)]

    def find_low_points(self):
        low_points = []
        for x, y in self.all_coords():
            nb_neighbours_higher = 0
            neighbours = self.neighbours4(x, y)
            for nx, ny in neighbours:
                if self.get(nx, ny) > self.get(x, y):
                    nb_neighbours_higher += 1
            if len(neighbours) == nb_neighbours_higher:
                low_points.append((x, y))
        return low_points


def parse(input: str) -> HeightMapGrid:
    return HeightMapGrid(input.split("\n"))


def part1(grid: HeightMapGrid) -> int:
    return sum(grid.get(x, y) + 1 for x, y in grid.find_low_points())


def find_basin(grid: HeightMapGrid, start):
    """Find the basin that contains the starting position using flood filling"""
    basin = [start]
    visited = [start]
    queue = deque(grid.neighbours4(start[0], start[1]))
    while len(queue) > 0:
        t = queue.popleft()
        if grid.get(t[0], t[1]) != 9 and t not in visited:
            basin.append(t)
            visited.append(t)

            for n in grid.neighbours4(t[0], t[1]):
                queue.append(n)

    return basin


def part2(grid):
    basins_sizes = [len(find_basin(grid, p)) for p in grid.find_low_points()]
    basins_sizes.sort(reverse=True)
    return prod(basins_sizes[:3])


test_grid = parse(test_input)
low_points = test_grid.find_low_points()

print(low_points[0])
print(find_basin(test_grid, low_points[0]))
print(part2(test_grid))

# print(test_grid)
grid = parse(input)
print(part2(grid))

assert (test_grid.is_in_grid(1, 1))
assert (not test_grid.is_in_grid(-1, 1))
assert (not test_grid.is_in_grid(1, -1))
assert (test_grid.is_in_grid(9, 0))
