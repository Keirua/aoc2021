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
        """Display these values as a 2-D grid.
        Inspired by norvig’s sudoku: http://norvig.com/sudoku.html
        """
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


def extract9(grid, p):
    offsets = [(-1, -1), (0, -1), (1, -1),
               (-1, 0), (0, 0), (1, 0),
               (-1, 1), (0, 1), (1, 1)]
    x, y = p
    out = ''
    for (dx, dy) in offsets:
        if grid.is_in_grid((x + dx, y + dy)):
            out += grid[(x + dx, y + dy)]
        else:
            out += '.'
    return out


def grid_to_i(s):
    return int(s.replace("#", "1").replace(".", "0"), 2)


def all_coords_plus_2(grid):
    for x in range(-1, grid.w + 1):
        for y in range(-1, grid.h + 1):
            yield x, y


def apply(mapping, grid: Grid):
    grid2 = Grid.from_value(grid.w + 2, grid.h + 2, 0)
    for (x, y) in all_coords_plus_2(grid):
        kernel = extract9(grid, (x, y))
        offset = grid_to_i(kernel)
        new_value = mapping[offset]

        grid2[(x + 1, y + 1)] = new_value

    return grid2


def part1(mapping, grid):
    grid2 = apply(mapping, grid)
    grid2 = apply(mapping, grid2)
    nb_lit = 0
    for c in grid2.all_coords():
        if grid2[c] == "#":
            nb_lit += 1
    # print(grid2)
    return nb_lit


mapping, grid = parse(input)
test_mapping, test_grid = parse(test_input)
# pp.pprint(mapping)
# print(grid)
# print(test_grid)
# print(extract9(test_grid, (2,2)))
# print(grid_to_i(extract9(test_grid, (2,2))))

# grid2 = apply(test_mapping, test_grid)
# print(grid2)
# assert(part1(test_mapping,test_grid) == 35)
print(part1(mapping, grid))  # not 5447 (too high)
