import aoc
import re, pprint, itertools as it

pp = pprint.PrettyPrinter(indent=4)

input = aoc.input_as_string(aoc.challenge_filename(22, 2021))
easy_input = aoc.input_as_string("input/22_2021_easy.txt")
medium_example = aoc.input_as_string("input/22_2021_medium.txt")

def parse(input):
    lines = aoc.as_lines(input)
    return [(l.startswith("on"), list(map(int, re.findall(r"(-?\d+)", l)))) for l in lines]

def part_1(instructions):
    grid = [[[False for _ in range(100+1)] for _ in range(100+1)] for _ in range(100+1)]
    for new_value, coords in instructions:
        xmin, xmax = max(-50, coords[0]), min(50, coords[1])
        ymin, ymax = max(-50, coords[2]), min(50, coords[3])
        zmin, zmax = max(-50, coords[4]), min(50, coords[5])

        for x, y, z in it.product(range(xmin, xmax+1), range(ymin, ymax+1), range(zmin, zmax+1)):
            try:
                grid[z+50][y+50][x+50] = new_value
            except IndexError as i:
                print(i, x, y, z)
                exit(0)
    # Count lit
    nb_lit = 0
    for x,y,z in it.product(range(100+1), range(100+1), range(100+1)):
        if grid[z][y][x] == True:
            nb_lit += 1
    return nb_lit

# instr  = parse(easy_input)
instr = parse(medium_example)
# instr = parse(input)
# pp.pprint(instr)
print(part_1(instr))