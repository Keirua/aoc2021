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
head_positions = [(0, 0)]
x, y = head_positions[-1]
for dir, dist in moves:
    dx, dy = mapping[dir]
    for i in range(dist):
        x += dx
        y += dy
        head_positions.append((x, y))


def plot(positions):
    W = max([x for (x, y) in positions]) + 1
    H = max([y for (x, y) in positions]) + 1
    arr = [["." for w in range(W)] for h in range(H)]
    for index, (x, y) in enumerate(positions):
        arr[y][x] = str(index)
    max_cell_size = max([len(arr[y][x]) for x in range(W) for y in range(H)])
    s = ""
    for y in range(H):
        s += "".join([c.center(1 + max_cell_size) for c in arr[H - y - 1]]) + "\n"
    return s


print(plot(head_positions))
print()
# print(len(set(head_positions[:-1])))
