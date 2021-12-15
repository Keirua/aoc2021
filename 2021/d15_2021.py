import aoc
import re, pprint, itertools as it
pp = pprint.PrettyPrinter(indent=4)

COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[92m"
COLOR_NORMAL = "\033[0m"

input = aoc.input_as_string(aoc.challenge_filename(15, 2021))
test_input = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""

lines = aoc.as_lines(input)
test_lines = aoc.as_lines(test_input)


class Grid:
    def __init__(self, w=0, h=0, lines=[]):
        self.w = w
        self.h = h
        self.lines = lines

    @classmethod
    def from_value(cls, w, h, value=0):
        return cls(w, h, [[value for _ in range(w)] for _ in range(h)])

    @classmethod
    def from_lines(cls, lines):
        return cls(len(lines[0]), len(lines), lines)

    def __setitem__(self, p, value):
        self.lines[p[1]][p[0]] = value

    def __getitem__(self, p):
        return self.lines[p[1]][p[0]]

    def set(self, x, y, v):
        self.lines[y][x] = v

    def get(self, x, y):
        return self.lines[y][x]

    def is_in_grid(self, p) -> bool:
        return 0 <= p[0] < self.w and 0 <= p[1] < self.h

    def neighbours4(self, p):
        """Return the neighbours, horizontal and vertical"""
        offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        x, y = p
        return [(x + dx, y + dy) for (dx, dy) in offsets if self.is_in_grid((x + dx, y + dy))]

    def neighbours8(self, p):
        """Return the eight neighbours, horijont, vertical and diagonals"""
        offsets = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        x, y = p
        return [(x + dx, y + dy) for (dx, dy) in offsets if self.is_in_grid((x + dx, y + dy))]

    def all_coords(self):
        for x in range(self.w):
            for y in range(self.h):
                yield x, y

    def get_cell_color(self, v):
        return COLOR_NORMAL

    def floodfill(self, start, cond_is_matched):
        """Find the neighbouring points using flood filling"""
        from collections import deque
        matching_points = [start]
        visited = [start]
        queue = deque(self.neighbours4(start))
        while len(queue) > 0:
            t = queue.popleft()
            if t not in visited and cond_is_matched(self[t]):
                matching_points.append(t)
                visited.append(t)

                for n in self.neighbours4(t):
                    queue.append(n)

        return matching_points

    def __str__(self):
        """Display these values as a 2-D grid.
        Inspired by norvig’s sudoku: http://norvig.com/sudoku.html
        """
        width = 1 + max([len(str(self.lines[y][x])) for (x, y) in self.all_coords()])
        text = ""
        for line in self.lines:
            text += ''.join([self.get_cell_color(c) + str(c).center(width) for c in line]) + "\n"
        return text + COLOR_NORMAL

def shortest_path(grid):
    start = (0,0)
    end = (grid.w-1, grid.h-1)
    path = []

test_grid = Grid.from_lines(test_lines)

print(test_grid)
shortest_path(test_grid)