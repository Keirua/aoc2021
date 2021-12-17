import aoc
import re, pprint, itertools as it

pp = pprint.PrettyPrinter(indent=4)

input = aoc.input_as_string(aoc.challenge_filename(17, 2021))


def parse(input):
    coords = list(map(int, list(re.findall(r"target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)", input)[0])))
    # x_min, x_max, y_min, y_max = coords
    return coords


def is_in_box(point, box_coords) -> bool:
    x, y = point
    x_min, x_max, y_min, y_max = box_coords
    return x >= x_min and x <= x_max and y >= y_min and y <= y_max


def launch(start, initial_vel, box_coords):
    x, y = start
    dx, dy = initial_vel
    max_y = y

    # for i in range(10000):
    while y > box_coords[2]: # y > min_y
        x = x + dx
        y = y + dy
        if dx > 0:
            dx -= 1
        if dy < 0:
            dx += 1
        dy -= 1
        max_y = max(max_y, y)
        if is_in_box((x, y), box_coords):
            return True, max_y
        # if x > box_coords[1] and y < box_coords[2]:
        #     break
    return False, 0


def part1(box_coords):
    start = (0, 0)
    max_y = 0
    for dx in range(1, box_coords[1]):
        for dy in range(-100, 100):
            in_box, y = launch(start, (dx, dy), box_coords)
            if in_box:
                if y > max_y:
                    print(dx, dy, max_y)
                max_y = max(max_y, y)
    return max_y

assert(launch((0,0), (6,9), (20, 30, -10, -5)) == (True, 45))
assert(launch((0,0), (17,-4), (20, 30, -10, -5)) == (False, 0))


assert (is_in_box((0, 0), (-1, 1, -1, 1)))
assert (is_in_box((0, 0), (-1, 1, 1, 2)) == False)
assert (is_in_box((0, 0), (1, 2, -1, 1)) == False)
# assert(part1((20, 30, -10, -5)) == 45)

coords = parse(input)
# print(coords)
print(part1(coords))