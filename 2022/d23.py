import pprint as pp


def parse(lines):
    elves = []
    for y, l in enumerate(lines):
        for x in range(len(l)):
            if l[x] == "#":
                elves.append((x, y))
    return elves


from collections import defaultdict


def partial_update(x, y, elves, direction, new_elves, next_direction):
    N = x, y - 1
    NE = x + 1, y - 1
    NW = x - 1, y - 1
    S = x, y + 1
    SE = x + 1, y + 1
    SW = x - 1, y + 1
    W = x - 1, y
    E = x + 1, y
    if all((other not in elves for other in [N, NE, NW, S, SE, SW, W, E])):
        return new_elves, next_direction
    ORDER = "NSWE"
    offset = ORDER.index(direction)
    order = [ORDER[(offset + i) % 4] for i in range(4)]
    # print(order)
    # print(len(elves))

    for direction in order:
        if direction == "N":
            if not (N in elves or NE in elves or NW in elves):
                new_elves[N].append((x, y))
                if next_direction is None:
                    next_direction = "S"
                break

        if direction == "S":
            if not (S in elves or SE in elves or SW in elves):
                new_elves[S].append((x, y))
                if next_direction is None:
                    next_direction = "W"
                break
        if direction == "W":
            if not (W in elves or NW in elves or SW in elves):
                new_elves[W].append((x, y))
                if next_direction is None:
                    next_direction = "E"
                break
        if direction == "E":
            if not (E in elves or NE in elves or SE in elves):
                new_elves[E].append((x, y))
                if next_direction is None:
                    next_direction = "N"
                break
    return new_elves, next_direction


def update(elves, direction):
    new_elves = defaultdict(list)
    next_direction = None
    # print(len(elves))
    # First half: where to go?
    for x, y in elves:
        new_elves, next_direction = partial_update(x, y, elves, direction, new_elves, next_direction)

    for k, v in new_elves.items():
        if len(v) == 1:
            elves.remove(v[0])
            elves.append(k)

    return elves, next_direction


def minmax(l):
    """Return both the min and max values in l"""
    mini = maxi = None
    for val in l:
        if mini is None or val < mini:
            mini = val
        if maxi is None or val > maxi:
            maxi = val
    return mini, maxi


def plot(elves):
    min_x, max_x = minmax([x for (x, y) in elves])
    min_y, max_y = minmax([y for (x, y) in elves])
    arr = []
    for y in range(min_y, max_y + 1):
        curr = []
        for x in range(min_x, max_x + 1):
            curr.append(".")
        arr.append(curr)

    for x, y in elves:
        arr[y - min_y][x - min_x] = "#"
    # pp.pprint(arr)
    return "\n".join(["".join(l) for l in arr])


def part1(elves):
    direction = "N"
    for i in range(10):
        elves, direction = update(elves, direction)
        print(f"Step {i}")
        print(plot(elves))

    min_x, max_x = minmax([x for (x, y) in elves])
    min_y, max_y = minmax([y for (x, y) in elves])
    print((max_y - min_y + 1) * (max_x - min_x + 1) - len(elves))
    print((max_y - min_y + 1) * (max_x - min_x + 1))


# lines = open(f"d23.txt").read().strip().splitlines()
# lines = open(f"d23-sample.txt").read().strip().splitlines()
lines = open(f"d23-sample2.txt").read().strip().splitlines()
elves = parse(lines)
# pp.pprint(elves)
# print(plot(elves))
# elves, direction = update(elves, "N")
# print(f"Step 1")
# print(plot(elves))
part1(elves)  # 5372 is too high
