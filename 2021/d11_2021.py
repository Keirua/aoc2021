import aoc
import re, pprint, itertools as it

pp = pprint.PrettyPrinter(indent=4)

COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[92m"
COLOR_NORMAL = "\033[0m"

input = aoc.input_as_string(aoc.challenge_filename(11, 2021))
lines = aoc.as_lines(input)
test_input = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

test_input2 = """11111
19991
19191
19991
11111"""
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
        offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        x, y = p
        return [(x + dx, y + dy) for (dx, dy) in offsets if self.is_in_grid((x + dx, y + dy))]

    def neighbours8(self, p):
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


class OctopusGrid(Grid):
    flashed = []

    """A grid to demo color implementation"""
    def __init__(self, w=0, h=0, lines=[]):
        super().__init__(w, h, lines)
        self.flashed = []

    def get_cell_color(self, v):
        return COLOR_GREEN if v != 0 else COLOR_RED

    def __str__(self):
        """Display these values as a 2-D grid.
        Inspired by norvig’s sudoku: http://norvig.com/sudoku.html
        """
        width = 1 + max([len(str(self.lines[y][x])) for (x, y) in self.all_coords()])
        text = ""
        for line in self.lines:
            text += ''.join([self.get_cell_color(c) + str(c).center(width) for c in line]) + "\n"
        return text + COLOR_NORMAL

    def step(self):
        output = OctopusGrid.from_value(self.w, self.h, 0)
        stk = []
        flashed = []
        for c in self.all_coords():
            output[c] = int(self[c])+1
            if output[c] > 9 and c not in flashed:
                stk.append(c)

        while len(stk) > 0:
            c = stk.pop()
            if c in flashed:
                continue
            flashed.append(c)
            for n in self.neighbours8(c):
                output[n] += 1
                if output[n] > 9 and n not in flashed:
                    stk.append(n)

        for f in flashed:
            output[f] = 0

        return output, len(flashed)

def part1(grid, n=3):
    total = 0
    for i in range(1, n+1):
        grid, nb = grid.step()
        total += nb
        print(f"Step {i}")
        print(grid)
    return total

def part2(grid):
    nb_steps = 0
    while True:
        grid, nb = grid.step()
        nb_steps +=1
        if nb == grid.w * grid.h:
            break
        # print(f"Step {nb_steps}")
        # print(grid)
    return nb_steps

grid = OctopusGrid.from_lines(lines)
test_grid = OctopusGrid.from_lines(test_lines)
test_grid2 = OctopusGrid.from_lines(aoc.as_lines(test_input2))
print(test_grid)
print(part1(test_grid, 10))
assert(part1(test_grid, 100) == 1656)
print(part1(grid, 100))
assert(part2(test_grid) == 195)
print(part2(grid))
