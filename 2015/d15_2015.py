import aoc
import re, pprint, itertools as it
pp = pprint.PrettyPrinter(indent=4)

input = aoc.input_as_string(aoc.challenge_filename(15, 2015))
test_input="""Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"""
def parse(input):
    parsed = re.findall(r"(.*): capacity ([-]?\d+), durability ([-]?\d+), flavor ([-]?\d+), texture ([-]?\d+), calories ([-]?\d+)", input)
    return [[int(cap), int(dur), int(flav), int(text), int(cal)] for (name, cap, dur, flav, text, cal) in parsed]

def score1(ingredient, nb_spoon):
    return sum([nb_spoon * ing for ing in ingredient[0:4]])

ingredients = parse(input)
# ingredients = parse(test_input)
pp.pprint(ingredients)
best_score = 0
from math import prod
# for a in range(1, 100):
#     for b in range(1, 100):
#         for c in range(1, 100):
#             for d in range(1, 100):
#                 if a+b+c+d == 100:
#                     s = [score1(ingredients[i], v) for (i,v) in enumerate([a,b,c,d])]
#                     print(s)
                    # s = score1(ingredients[0], a)*score1(ingredients[1], b)*score1(ingredients[2], c)*score1(ingredients[3], d)
                    # if s > best_score:
                    #     best_score = s
print(best_score)

# pp.pprint(score1(ingredients[0], 44))
# pp.pprint(score1(ingredients[1], 56))
