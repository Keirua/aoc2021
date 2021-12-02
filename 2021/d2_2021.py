import aoc
import re

test_input="""forward 5
down 5
forward 8
up 3
down 8
forward 2"""
input = aoc.input_as_string(aoc.challenge_filename(2, 2021))

def parse(input):
    matches = re.findall(r"(up|down|forward|) (\d+)", input)
    return [(m, int(q)) for m, q in matches]

def part1(instructions):
    depth, x = 0,0
    for (m, q) in instructions:
        if m == "forward":
            x += q
        if m == "up":
            depth -= q
        if m == "down":
            depth += q
    return depth * x

def part2(instructions):
    depth, x, aim = 0,0,0
    for (m, q) in instructions:
        if m == "forward":
            x += q
            depth += aim * q
        if m == "up":
            aim -= q
        if m == "down":
            aim += q
    return depth * x

assert(part1(parse(test_input)) == 150)
assert(part2(parse(test_input)) == 900)

instructions = parse(input)
print(part1(instructions))
print(part2(instructions))