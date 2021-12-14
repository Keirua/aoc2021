import aoc
import re, pprint, itertools as it
pp = pprint.PrettyPrinter(indent=4)

input = aoc.input_as_string(aoc.challenge_filename(13, 2021))
test_input = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""
# lines = aoc.as_lines(input)


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

    def is_in_grid(self, p) -> bool:
        return 0 <= p[0] < self.w and 0 <= p[1] < self.h

    def all_coords(self):
        for x in range(self.w):
            for y in range(self.h):
                yield x, y

    def __str__(self):
        """Display these values as a 2-D grid.
        Inspired by norvig’s sudoku: http://norvig.com/sudoku.html
        """
        width = 1
        text = ""
        for line in self.lines:
            text += ''.join([str(c).center(width) for c in line]) + "\n"
        return text

def parse(input):
    # lines = input.split("\n")
    coords = [(int(x), int(y)) for (x, y) in re.findall(r"(\d+),(\d+)", input)]
    folds = [(axis, int(v)) for axis,v in re.findall(r"(x|y)=(\d+)", input)]
    max_x = max(x for (x, y) in coords)
    max_y = max(y for (x, y) in coords)
    # print(max_x, max_y)
    g = Grid.from_value(max_x+1, max_y+1, ".")
    # print(coords)
    for c in coords:
        g[c] = "█"

    return (g, folds)

def fold(grid:Grid, fold):
    axis, value = fold
    # print(axis, value, fold)
    if axis == 'y':
        g2 = Grid.from_value(grid.w, value, '.')
        for c in grid.all_coords():
            # before the fold line, we copy the content
            if c[1] < value and grid[c] != ".":
                g2[c] = grid[c]
            # after the fold line, we mirror the result
            if c[1] > value  and grid[c] != ".":
                mirror_pos = value - (c[1]-value)
                if mirror_pos >=0:
                    g2[(c[0], mirror_pos)] = grid[c]
        return g2
    if axis == 'x':
        g2 = Grid.from_value(value, grid.h, '.')
        for c in grid.all_coords():
            # before the fold line, we copy the content
            if c[0] < value and grid[c] != ".":
                g2[c] = grid[c]
            # after the fold line, we mirror the result
            if c[0] > value and grid[c] != ".":
                mirror_pos = value - (c[0] - value)
                if mirror_pos >= 0:
                    g2[(mirror_pos, c[1])] = grid[c]
        return g2

def part2(grid, folds):
    for f in folds:
        grid = fold(grid, f)
    print(grid)

def part1(grid:Grid, folds):
    grid = fold(grid, folds[0])
    nb_lit = 0
    for c in grid.all_coords():
        if grid[c] == "█":
            nb_lit += 1
    return nb_lit

grid, folds = parse(input)
test_grid, test_folds = parse(test_input)

assert(part1(test_grid, test_folds) ==17)
print(part1(grid, folds))
part2(grid, folds) # CPJBERUL