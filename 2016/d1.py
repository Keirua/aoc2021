import pprint as pp


def dist(x, y): return abs(x) + abs(y)


input = open(f"d1.txt").read().strip()
instructions = input.split(", ")
x, y = 0, 0
dx, dy = 0, 1
locations = set()
p2 = None

for instr in instructions:
    dir, amount = instr[0], int(instr[1:])
    if dir == 'R':
        dx, dy = -dy, dx
    else:
        dx, dy = dy, -dx
    for i in range(amount):
        x, y = x + dx, y + dy
        if (x, y) in locations and p2 is None:
            p2 = dist(x, y)
        locations.add((x, y))
p1 = dist(x, y)
print(p1)
print(p2)
