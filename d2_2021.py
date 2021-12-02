import aoc
import re, pprint, itertools as it
pp = pprint.PrettyPrinter(indent=4)

input="""forward 5
down 5
forward 8
up 3
down 8
forward 2"""
input = aoc.input_as_string(aoc.challenge_filename(2, 2021))
matches = re.findall(r"(up|down|forward|) (\d+)", input)
instructions = [(m, int(q)) for m, q in matches]

depth, x = 0,0
for (m, q) in instructions:
    if m == "forward":
        x += q
    if m == "up":
        depth -= q
    if m == "down":
        depth += q


pp.pprint(instructions)
print(depth*x)