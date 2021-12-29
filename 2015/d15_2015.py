import aoc
import re, pprint, itertools as it
pp = pprint.PrettyPrinter(indent=4)

input = aoc.input_as_string(aoc.challenge_filename(15, 2015))
test_input="""Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"""
def parse(input):
    parsed = re.findall(r"(.*): capacity ([-]?\d+), durability ([-]?\d+), flavor ([-]?\d+), texture ([-]?\d+), calories ([-]?\d+)", input)
    return [[int(cap), int(dur), int(flav), int(text), int(cal)] for (name, cap, dur, flav, text, cal) in parsed]

# We want to find the different ways to write n as the sum of k positive numbers
def different_ways(n, k, l=[]):
    out = []
    if len(l) < k:
        for i in range(0, n+1):
            out += different_ways(n-i, k-1, l+[i])
    else:
        out.append(l+[n])
    return out

# pp.pprint(different_ways(10, 4+1, []))
# pp.pprint(different_ways(10, 3+1, []))


def scalar(a,b):
    return sum(u*v for u,v in zip(a,b))

assert(scalar([44, 56], [-1, 2]) == 68)

def part1(ingredients):
    best_score = 0
    for ways in different_ways(100, len(ingredients)+1):
        score = 1
        for component in range(4+1):
            ingredient_components = []
            for ingredient in ingredients:
                ingredient_components.append(ingredient[component])
            score *= scalar(ingredient_components, ways)
            print(scalar(ingredient_components, ways))
        if score > best_score:
            best_score = score
    return best_score

ingredients = parse(input)
test_ingredients = parse(test_input)
assert(part1(test_ingredients) == 62842880), part1(test_ingredients)

