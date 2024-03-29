import aoc
import re, pprint, itertools as it

pp = pprint.PrettyPrinter(indent=4)

input = aoc.input_as_string(aoc.challenge_filename(22, 2021))
easy_input = aoc.input_as_string("input/22_2021_easy.txt")
medium_example = aoc.input_as_string("input/22_2021_medium.txt")
part2_example = aoc.input_as_string("input/22_2021_part2.txt")


def parse(input):
    lines = aoc.as_lines(input)
    return [(l.startswith("on"), list(map(int, re.findall(r"(-?\d+)", l)))) for l in lines]


def part1(instructions):
    grid = [[[False for _ in range(100 + 1)] for _ in range(100 + 1)] for _ in range(100 + 1)]
    for new_value, coords in instructions:
        xmin, xmax = max(-50, coords[0]), min(50, coords[1])
        ymin, ymax = max(-50, coords[2]), min(50, coords[3])
        zmin, zmax = max(-50, coords[4]), min(50, coords[5])

        for x, y, z in it.product(range(xmin, xmax + 1), range(ymin, ymax + 1), range(zmin, zmax + 1)):
            try:
                grid[z + 50][y + 50][x + 50] = new_value
            except IndexError as i:
                print(i, x, y, z)
                exit(0)
    # Count lit
    nb_lit = 0
    for x, y, z in it.product(range(100 + 1), range(100 + 1), range(100 + 1)):
        if grid[z][y][x] == True:
            nb_lit += 1
    return nb_lit


def cubies(coords):
    xmin, xmax = coords[0], coords[1]
    ymin, ymax = coords[2], coords[3]
    zmin, zmax = coords[4], coords[5]

    return set(
        [(x, y, z) for x, y, z in it.product(range(xmin, xmax + 1), range(ymin, ymax + 1), range(zmin, zmax + 1))])


def bounded_cubies(coords):
    xmin, xmax = max(-50, coords[0]), min(50, coords[1])
    ymin, ymax = max(-50, coords[2]), min(50, coords[3])
    zmin, zmax = max(-50, coords[4]), min(50, coords[5])

    return set(
        [(x, y, z) for x, y, z in it.product(range(xmin, xmax + 1), range(ymin, ymax + 1), range(zmin, zmax + 1))])


def part1_list(instr):
    cubes = set()
    for new_value, coords in instr:
        if new_value:
            cubes = cubes | bounded_cubies(coords)
        else:
            intersection = cubes & bounded_cubies(coords)
            cubes -= intersection
    return len(cubes)


def part2_csg(instr):
    """
    so in this part, we are making a CSG object with intersection and differences:
    https://www.reddit.com/r/gamedev/comments/q9tvs/constructive_solid_geometry_csg_subtract_algorithm/
    https://www.reddit.com/r/gamedev/comments/q9tvs/constructive_solid_geometry_csg_subtract_algorithm/
    We need to keep track of a giant object which is composed of many cubes, all of them part of the ON cubes.
    Then we have 2 situations to cover:
     - a cube OFF intersects a cube ON -> we remove the difference
     - a cube ON intersects cube ON -> we intersect the 2 cubes in order to not have duplicates
    """
    pass

    # print(coords, volume(coords))
    # a list of all the axis-aligned cubes containing lit cubes
    # lit_cubes = []
    # for new_value, coords in instr:
    #     if new_value:
    #         for l in lit_cubes:
    #             if cube_intersect(l, coords):
    #                 raise ValueError("I don’t know what to do")
    #         lit_cubes.append(coords)


def volume(c):
    """compute the volume of a cube, given its coordinates"""
    return (c[1] + 1 - c[0]) * (c[3] + 1 - c[2]) * (c[5] + 1 - c[4])

def volume2(c):
    """compute the volume of a cube, given its coordinates"""
    return (c[1] - c[0]) * (c[3] - c[2]) * (c[5] - c[4])

def compress_coords(instructions):
    x_coords = set()
    y_coords = set()
    z_coords = set()
    for new_val, coords in instructions:
        x_coords |= set([coords[0], coords[1]])
        y_coords |= set([coords[2], coords[3]])
        z_coords |= set([coords[4], coords[5]])
    x_coords = sorted(x_coords)
    y_coords = sorted(y_coords)
    z_coords = sorted(z_coords)
    return x_coords, y_coords, z_coords


def part2(instructions) -> int:
    """
    ok, so I was lost, didn’t want to perform CSG because splitting a cube into many
    smaller cubes. I opened reddit, a keyword came up: coordinates compression.

    https://www.quora.com/What-is-coordinate-compression-and-what-is-it-used-for?share=1
    """
    x_coords, y_coords, z_coords = compress_coords(instructions)
    print(len(x_coords), len(y_coords), len(z_coords))
    grid = [[[False for _ in range(len(x_coords) + 1)] for _ in range(len(y_coords) + 1)] for _ in
            range(len(z_coords) + 1)]
    for new_value, coords in instructions:
        # We compute the compressed coordinates for this cube
        xmin, xmax = x_coords.index(coords[0]), x_coords.index(coords[1])
        ymin, ymax = y_coords.index(coords[2]), y_coords.index(coords[3])
        zmin, zmax = z_coords.index(coords[4]), z_coords.index(coords[5])
        for x, y, z in it.product(range(xmin, xmax + 1), range(ymin, ymax + 1), range(zmin, zmax + 1)):
            try:
                grid[z][y][x] = new_value
            except IndexError as i:
                print(i, x, y, z)
                exit(0)
    # Count lit
    nb_lit = 0
    for z, y, x in it.product(range(len(z_coords)-1), range(len(y_coords)-1), range(len(x_coords)-1)):
        if grid[z][y][x]:
            x_min, x_max = x_coords[x], x_coords[x + 1]
            y_min, y_max = y_coords[y], y_coords[y + 1]
            z_min, z_max = z_coords[z], z_coords[z + 1]
            nb_lit += volume2([x_min, x_max, y_min, y_max, z_min, z_max])
    return nb_lit


def cube_intersect(a, b):
    """do axis-aligned cubes a and b intersect?"""
    # https://stackoverflow.com/a/3631603
    return (a[1] >= b[0] and a[0] <= b[1]) and (a[3] >= b[2] and a[2] <= b[3]) and (a[5] >= b[4] and a[4] <= b[5])
    # return (a[.max_x()] >= b.min_x() and a.min_x() <= b.max_x())
    # and (a.max_y() >= b.min_y() and a.min_y() <= b.max_y())
    # and (a.max_z() >= b.min_z() and a.min_z() <= b.max_z())


# x=10..10,y=10..10,z=10..10 turns on a single cube, 10,10,10 -> volume 1
# assert (volume([10, 10, 10, 10, 10, 10]) == 1)
# 9..11,y=9..11,z=9..11 is a 3x3x3 cube, with volume 27
# assert (volume([9, 11, 9, 11, 9, 11]) == 27)

easy_instr = parse(easy_input)
print(easy_instr)
# medium_instr = parse(medium_example)
part2_instr = parse(part2_example)
# instr = parse(input)
# pp.pprint(instr)
# assert(part(medium_instr) == 590784)
# assert(part1_list(medium_instr) == 590784)
assert (part1_list(easy_instr) == 39), part1_list(easy_instr)
assert (part2(part2_instr) == 2758514936282235), part2(part2_instr)
# assert(part2(easy_instr) == 39)
# print(part2(medium_instr))
# print(part_1(instr))
