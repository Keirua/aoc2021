import re, pprint
pp = pprint.PrettyPrinter(indent=4)

def parse(text):
    coords = []
    for line in text.split("\n"):
        coords.append(tuple(int(c) for c in re.findall(r"(-?\d+)", line)))
    return coords

deltas = [(-1,0,0), (1,0,0), (0,-1,0), (0,1,0), (0,0,-1), (0, 0, 1)]

text = open(f"d18.txt").read().rstrip()
text_sample = open(f"d18-sample.txt").read().rstrip()
coords = parse(text)
coords_sample = parse(text_sample)
text_unit = """1,1,1
2,1,1"""
coords_unit = parse(text_unit)

def part1(coords, deltas):
    connections = {c: set() for c in coords}
    for i in range(len(coords)):
        for j in range(i+1, len(coords)):
            x, y, z = coords[i]
            x2, y2, z2 = coords[j]
            dx, dy, dz = x2-x, y2-y, z2-z
            if (dx, dy, dz) in deltas:
                connections[(x, y, z)].add((dx, dy, dz))
                dx2, dy2, dz2 = -dx, -dy, -dz
                connections[(x2, y2, z2)].add((dx2, dy2, dz2))

    surfaces = sum(len(deltas) - len(connections[c]) for c in coords)
    return surfaces

print(part1(coords_sample, deltas))
print(part1(coords_unit, deltas))
print(part1(coords, deltas))
# prir
# print(surfaces) # 10694 is too high
# pp.pprint(coords)
