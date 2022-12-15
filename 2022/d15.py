import re

def parse(text):
    positions = [list(map(int, re.findall("(-?\d+)", l))) for l in text.strip().split("\n")]
    # beacons = []
    # for (x, y, x2, y2) in positions:
    #     beacons.append((x,y))
    #     beacons.append((x2,y2))
    return positions

def manhattan_distance(x, y, x2, y2):
    """https://en.wikipedia.org/wiki/Taxicab_geometry"""
    return abs(x2 - x) + abs(y2 - y)

def part1(positions, y0=2000000):
    not_possible = []
    for (x, y, x2, y2) in positions:
        dist = manhattan_distance(x, y, x2, y2)
        dx = dist - abs(y0-y)
        if dx < 0:
            continue
        for curr_x in range(dx+1):
            if (x+curr_x, y0) != (x2, y2):
                not_possible.append(x+curr_x)
            if (x-curr_x, y0) != (x2, y2):
                not_possible.append(x-curr_x)
    return len(set(not_possible))


text_sample = open(f"d15-sample.txt").read()
d15_pos_sample = parse(text_sample)
text = open(f"d15.txt").read()
d15_pos = parse(text)

print(part1(d15_pos_sample, 10))
print(part1(d15_pos))
# print(part1(d15_pos)) # 4720524 is too low, 5461727 is too low, 5461730 is too high, 5461729 is good

# pp.pprint(positions)
