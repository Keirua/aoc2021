import aoc
import re, pprint, itertools as it
pp = pprint.PrettyPrinter(indent=4)

input = open(f"d1.txt").read().strip()
instructions = input.split(", ")
x, y = 0,0
dx, dy = 0,1
for instr in instructions:
    dir, amount = instr[0], int(instr[1:])
    if dir == 'R':
        dx, dy = -dy, dx
    else:
        dx, dy = dy, -dx
    x, y = x + dx*amount, y+dy*amount
    print(x,y, dy, dy)
print(abs(x)+abs(y))


# pp.pprint(lines)
