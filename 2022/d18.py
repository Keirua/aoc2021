import re, pprint
pp = pprint.PrettyPrinter(indent=4)

def parse(text):
    coords = []
    for line in text.split("\n"):
        coords.append(tuple(int(c) for c in re.findall(r"(-?\d+)", line)))
    return coords

deltas = [(-1,0,0), (1,0,0), (0,-1,0), (0,1,0), (0,0,-1), (0, 0, 1)]

class MiniSet():
    def __init__(self):
        self.content = 0

    def add(self, v):
        global deltas
        try:
            index = deltas.index(v)
            self.content |= 1<<index
        except:
            pass
    def __len__(self):
        return self.content.bit_count() # Number of ones in the binary representation of the absolute value

text = open(f"d18.txt").read().rstrip()
text_sample = open(f"d18-sample.txt").read().rstrip()
coords = parse(text)
coords_sample = parse(text_sample)
text_unit = """1,1,1
2,1,1"""
coords_unit = parse(text_unit)

def part1(coords, deltas):
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

def extract_bbox(coords):
    """extract the bounding box of the list on vertices"""
    minx, miny, minz = coords[0]
    maxx, maxy, maxz = coords[0]
    for i in range(1, len(coords)):
        x, y, z = coords[i]
        minx, miny, minz = min(minx, x), min(miny, y), min(minz, z)
        maxx, maxy, maxz = max(maxx, x), max(maxy, y), max(maxz, z)
    # Taking a bit of margin here
    return minx-1, miny-1, minz-1, maxx+1, maxy+1, maxz+1

def flood_fill_3d(coords, deltas):
    """
    part 2 = we remove the connections from the points inside the shape
    We find the outer points by floodfilling for a point inside the bounding box
    then we can create the connections with the rest of the coords
    """
    minx, miny, minz, maxx, maxy, maxz = extract_bbox(coords)
    Q = [(minx, miny, minz)]
    SEEN = []
    outer_shell = []
    while(len(Q)) > 0:
        x, y, z = Q.pop()
        for dx, dy, dz in deltas:
            nx, ny, nz = x+dx, y+dy, z+dz
            if minx <= nx <= maxx and miny <= ny <= maxy and minz <= nz <= maxz:
                if (nx, ny, nz) not in SEEN:
                    if (nx, ny, nz) not in coords:
                        Q.append((nx, ny, nz))
                        outer_shell.append((nx, ny, nz))

                    SEEN.append((nx, ny, nz))
    # Now we have a list of all the cells on the outer shell, we can then deduce the coords on the inner shell
    for x in range(minx, maxx+1):
        for y in range(miny, maxy+1):
            for z in range(minz, maxz+1):
                if (x, y, z) not in outer_shell and (x, y, z) not in coords:
                    # then (x, y, z) is inside the shell
                    for (x2, y2, z2) in coords:
                        dx, dy, dz = x-x2, y-y2, z-z2
                        if (dx, dy, dz) in deltas:
                            connections[(x2, y2, z2)].add((dx, dy, dz))
    surfaces = sum(len(deltas) - len(connections[c]) for c in coords)
    return surfaces

# coords = coords_sample
# connections = {c: MiniSet() for c in coords}
connections = {c: set() for c in coords}
part1(coords, deltas)
print(extract_bbox(coords))
print(flood_fill_3d(coords, deltas))

# print(part1(coords_sample, deltas))
# print(part1(coords_unit, deltas))
# print(part1(coords, deltas))
# prir
# print(surfaces) # 10694 is too high
# pp.pprint(coords)
