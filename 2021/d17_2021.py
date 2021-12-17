import re
import aoc


def parse(input):
    return list(map(int, list(re.findall(r"target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)", input)[0])))


def is_in_box(point, box_coords) -> bool:
    x, y = point
    x_min, x_max, y_min, y_max = box_coords
    return x_min <= x <= x_max and y_min <= y <= y_max


def launch(start, initial_vel, box_coords):
    x, y = start
    dx, dy = initial_vel
    max_y = y

    while y > box_coords[2]:  # y > min_y
        x = x + dx
        y = y + dy
        if dx > 0: dx -= 1
        if dx < 0: dx += 1
        dy -= 1
        max_y = max(max_y, y)
        if is_in_box((x, y), box_coords):
            return True, max_y
        if x > box_coords[1] and y < box_coords[2]:
            break
    return False, 0


def part1(box_coords, start=(0, 0)) -> int:
    max_y = 0
    for dx in range(1, box_coords[1]):
        for dy in range(-50, 50):  # dirty hardcoding, so what?
            in_box, y = launch(start, (dx, dy), box_coords)
            if in_box:
                max_y = max(max_y, y)
    return max_y


# List on some points
# debug_vel = [(23,-10),(25,-7),(8,0),(26,-10),(20,-8),(25,-6),(25,-10),(8,1),(24,-10),(7,5),(23,-5),(27,-10),(8,-2),(25,-9),(27,-5),(29,-6),(22,-6),(21,-7),(9,0),(27,-7),(24,-5),(26,-6),(25,-5),(6,8),(11,-2),(20,-5),(29,-10),(6,3),(28,-7),(30,-6),(29,-8),(20,-10),(6,7),(6,4),(6,1),(14,-4),(21,-6),(7,-1),(7,7),(8,-1),(21,-9),(6,2),(20,-7),(30,-10),(14,-3),(13,-2),(7,3),(28,-8),(29,-9),(15,-3),(22,-5),(26,-8),(25,-8),(15,-4),(9,-2),(15,-2),(12,-2),(28,-9),(12,-3),(24,-6),(23,-7),(7,8),(11,-3),(26,-7),(7,1),(23,-9),(6,0),(22,-10),(27,-6),(22,-8),(13,-4),(7,6),(28,-6),(11,-4),(12,-4),(26,-9),(7,4),(23,-8),(30,-8),(7,0),(9,-1),(10,-1),(26,-5),(22,-9),(6,5),(23,-6),(28,-10),(10,-2),(11,-1),(20,-9),(14,-2),(29,-7),(13,-3),(24,-8),(27,-9),(30,-7),(28,-5),(21,-10),(7,9),(6,6),(21,-5),(7,2),(30,-9),(21,-8),(22,-7),(24,-9),(20,-6),(6,9),(29,-5),(27,-8),(30,-5),(24,-7)]
def part2(box_coords, start=(0,0)) -> int:
    nb_inside = 0
    velocities = []

    for dx in range(1, box_coords[1] + 1):
        for dy in range(-100, 100):
            in_box, y = launch(start, (dx, dy), box_coords)
            if in_box:
                velocities.append((dx, dy))
                nb_inside += 1

    return nb_inside


input = open(aoc.challenge_filename(17, 2021)).read()
test_box = (20, 30, -10, -5)
box = parse(input)
assert (launch((0, 0), (6, 9), (20, 30, -10, -5)) == (True, 45))
assert (launch((0, 0), (17, -4), (20, 30, -10, -5)) == (False, 0))
assert (is_in_box((0, 0), (-1, 1, -1, 1)))
assert (is_in_box((0, 0), (-1, 1, 1, 2)) == False)
assert (is_in_box((0, 0), (1, 2, -1, 1)) == False)
assert (part1(test_box) == 45)
print(part1(box))
assert (part2(test_box) == 112)
print(part2(box))  # 1116 is too low
