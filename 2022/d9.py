import re, pprint, itertools as it
pp = pprint.PrettyPrinter(indent=4)

input = open(f"d9.txt").read()
input = open(f"d9-sample.txt").read()
moves = [(dir, int(dist)) for (dir, dist) in re.findall(r"([RDLU]) (\d+)", input)]
mapping = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1),
}
positions = []
x, y = 0, 0
for dir, dist in moves:
    dx, dy = mapping[dir]
    for i in range(dist):
        x+=dx
        y+=dy
        positions.append((x, y))
print(len(set(positions[:-1])))

