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


def parse_grid(lines):
    w = len(lines[0])
    h = len(lines)
    lit_points = []
    for y in range(h):
        for x in range(w):
            if lines[y][x] == "#":
                lit_points.append((x, y))
    return Grid(0, 0, w, h, lit_points)


def parse(input):
    lines = aoc.as_lines(input)
    mapping = lines[0]
    return mapping, parse_grid(lines[2:])


class Grid:
    def __init__(self, min_x, min_y, max_x, max_y, lit_points):
        self.max_x = max_x
        self.max_y = max_y
        self.min_x = min_x
        self.min_y = min_y
        self.lit_points = lit_points

    def all_coords(self):
        for x in range(self.min_x, self.max_x + 1):
            for y in range(self.min_y, self.max_y + 1):
                yield x, y

    def extract9(self, p):
        offsets = [(-1, -1), (0, -1), (1, -1),
                   (-1, 0), (0, 0), (1, 0),
                   (-1, 1), (0, 1), (1, 1)]
        x, y = p
        out = ''
        for (dx, dy) in offsets:
            if (x + dx, y + dy) in self.lit_points:
                out += "1"
            else:
                out += "0"
        return int(out, 2)

    def __str__(self):
        off_x, off_y = 0, 0
        if self.min_x < 0:
            off_x = -self.min_x
        if self.min_y < 0:
            off_y = -self.min_y

        lines = [["." for _ in range(self.min_x, self.max_x+1)] for _ in range(self.min_y, self.max_y+1)]
        for (x, y) in self.lit_points:
            lines[y + off_y][x + off_x] = "#"
        return "\n".join(["".join(l) for l in lines])


def apply(mapping, grid: Grid):
    grid2 = Grid(grid.min_x - 1, grid.min_y - 1, grid.max_x + 1, grid.max_y + 1, [])

    for (x, y) in grid2.all_coords():
        offset = grid.extract9((x, y))
        new_value = mapping[offset]
        if new_value == "#":
            grid2.lit_points.append((x, y))

    print(grid2)
    return grid2


def part1(mapping, grid):
    for i in range(2):
        grid = apply(mapping, grid)
    return len(grid.lit_points)


mapping, grid = parse(input)
test_mapping, test_grid = parse(test_input)
print(test_grid)

# grid2 = apply(test_mapping, test_grid)
assert (part1(test_mapping, test_grid) == 35)
print(part1(mapping, grid))
