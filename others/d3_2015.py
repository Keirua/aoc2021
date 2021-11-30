import aoc
import re, pprint, itertools as it
pp = pprint.PrettyPrinter(indent=4)

input = aoc.input_as_string(aoc.challenge_filename(3, 2015))
# lines = aoc.as_lines(input)
mapping = {
    '<': (-1, 0),
    '>': (1, 0),
    'v': (0, 1),
    '^': (0, -1),
}

def count_houses(input):
    x, y = (0, 0)
    houses = [(x, y)]
    for m in input:
        dx, dy = mapping[m]
        x, y = x+dx, y+dy
        houses.append((x,y))

    return len(set(houses))

def count_houses_with_robo(input):
    xs, ys = (0, 0)
    xr, yr = (0, 0)
    houses = [(0, 0)]
    for i,m in enumerate(input):
        dx, dy = mapping[m]
        if i%2 == 0:
            xs, ys = xs+dx, ys+dy
            houses.append((xs, ys))
        else:
            xr, yr = xr+dx, yr+dy
            houses.append((xr,yr))

    return len(set(houses))

assert(count_houses(">") == 2)
assert(count_houses("^>v<") == 4)
assert(count_houses("^v^v^v^v^v") == 2)
print(count_houses(input))

assert(count_houses_with_robo("^v") == 3)
assert(count_houses_with_robo("^>v<") == 3)
assert(count_houses_with_robo("^v^v^v^v^v") == 11)
print(count_houses_with_robo(input))
