import re, pprint, itertools as it

pp = pprint.PrettyPrinter(indent=4)

input = open(f"d9.txt").read()
# input = open(f"d9-sample.txt").read()
moves = [(dir, int(dist)) for (dir, dist) in re.findall(r"([RDLU]) (\d+)", input)]
mapping = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1),
}
head_positions = [(0, 0)]
tail_positions = [(0, 0)]

for dir, dist in moves:
    dx, dy = mapping[dir]
    for i in range(dist):
        xh, yh = head_positions[-1]
        xt, yt = tail_positions[-1]
        # Compute the new head position
        xh, yh = xh+ dx, yh + dy
        # Compute the movement between new head and previous tail
        dthx, dthy = xh - xt, yh - yt
        # If we moved enough, we need to update the tail to the previous head position
        if abs(dthx) > 1 or abs(dthy) > 1:
            tail_positions.append(head_positions[-1])
        head_positions.append((xh, yh))

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


# print(plot(head_positions))
# print()
# print(plot(tail_positions))
print(len(set(tail_positions)))
# print(len(set(head_positions[:-1])))
