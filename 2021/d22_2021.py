import aoc
import re, pprint, itertools as it

pp = pprint.PrettyPrinter(indent=4)

input = aoc.input_as_string(aoc.challenge_filename(22, 2021))
easy_input = aoc.input_as_string("input/22_2021_easy.txt")
medium_example = aoc.input_as_string("input/22_2021_medium.txt")

def parse(input):
    lines = aoc.as_lines(input)
    return [(l.startswith("on"), list(map(int, re.findall(r"(-?\d+)", l)))) for l in lines]


instr  = parse(easy_input)
instr = parse(medium_example)
instr = parse(input)
pp.pprint(instr)
