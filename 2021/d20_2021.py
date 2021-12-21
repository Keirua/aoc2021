import aoc
import re, pprint, itertools as it

pp = pprint.PrettyPrinter(indent=4)

input = aoc.input_as_string(aoc.challenge_filename(20, 2021))

test_input = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###"""


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
        width = 1
        if self.w < 100:
            width = 1 + max([len(str(self.lines[y][x])) for (x, y) in self.all_coords()])
        text = ""
        for line in self.lines:
            text += ''.join([str(c).center(width) for c in line]) + "\n"
        return text


def parse(input):
    lines = aoc.as_lines(input)
    mapping = lines[0]
    grid = Grid.from_lines((lines[2:]))
    return mapping, grid


def extract9(grid, p, default="."):
    x, y = p
    out = ''
    for y2 in range(y-1, y+2):
        for x2 in range(x-1, x+2):
            if grid.is_in_grid((x2, y2)):
                out += grid[(x2, y2)]
            else:
                out += default
    return out


def grid_to_i(s):
    return int(s.replace("#", "1").replace(".", "0"), 2)


def apply(mapping, grid: Grid, default='.'):
    grid2 = Grid.from_value(grid.w + 2, grid.h + 2, default)
    for (x, y) in grid2.all_coords():
        kernel = extract9(grid, (x-1, y-1), default)
        offset = grid_to_i(kernel)
        grid2[(x, y)] = mapping[offset]

    return grid2


def part1(mapping, grid, nb_steps=2):
    for i in range(nb_steps):
        default = '#'
        if i%2 == 0:
            default = "."
        grid = apply(mapping, grid, default)
        # print(grid)
    return sum(grid[c] == "#" for c in grid.all_coords())


mapping, grid = parse(input)
test_mapping, test_grid = parse(test_input)
assert(grid_to_i(extract9(test_grid, (2,2))) == 34)

print(test_grid)
# part1(test_mapping, test_grid)
# assert(part1(test_mapping,test_grid) == 35)
print(part1(mapping, grid))  # not 5447 (too high)
print(part1(mapping, grid, 50))  # not 5447 (too high)
