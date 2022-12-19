import re, pprint
pp = pprint.PrettyPrinter(indent=4)

def parse_costs(a):
    c, n = a
    return int(c), n

def parse(text):
    out = []
    for blueprint in text.split("\n\n"):
        # Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 14 clay. Each geode robot costs 2 ore and 16 obsidian.
        for line in blueprint.split("\n"):
            costs = re.findall("((\d+) (ore|clay|geode|obsidian))+", line)
            w = line.split(" ")
            blueprint = {}
            blueprint[w[3]] = [parse_costs(costs[0][1:])]
            blueprint[w[9]] = [parse_costs(costs[1][1:])]
            blueprint[w[15]] = [parse_costs(costs[2][1:]), parse_costs(costs[3][1:])]
            blueprint[w[24]] = [parse_costs(costs[4][1:]), parse_costs(costs[5][1:])]

            # print(line)
            # print(costs)
            # pp.pprint(blueprint)
            out.append(blueprint)
    return out
from functools import lru_cache

def compute_new_ressources(ressources, robots):
    new_ressources = ressources.copy()
    for k, v in robots.items():
        new_ressources[k] += v
    return new_ressources


def best_spend(blueprint, step, ressources, robots):
    if step == 0:
        return ressources["geode"]
    else:
        possible_scores = [ressources["geode"]]
        for ressource_name, costs in blueprint.items():
            # If we have enough ressources to produce said robots, we can build one:
            if all([ressources[name] > cost for cost, name in costs]):
                new_ressources = ressources.copy()
                new_robots = robots.copy()
                # new_ressources[name] += 1
                for cost, name in costs:
                    new_ressources[name] -= cost
                new_robots[ressource_name] += 1
                new_ressources = compute_new_ressources(new_ressources, robots)
                # New edge -> buying a new robot
                possible_scores.append(best_spend(blueprint, step-1, new_ressources, new_robots))
        # Then we can also dig for the ressources we own without buying right now
        new_ressources = compute_new_ressources(ressources, robots)
        possible_scores.append(best_spend(blueprint, step - 1, new_ressources, robots))
        return max(possible_scores)


ressources_names = ["ore", "clay", "obsidian", "geode"]
text = open(f"d19.txt").read().strip()
text_sample = open(f"d19-sample.txt").read().strip()
# pp.pprint(parse(text))
# pp.pprint()
blueprints = parse(text_sample)
from collections import defaultdict
robots = defaultdict(int)
robots["ore"] = 1
print(best_spend(blueprints[0], 24, defaultdict(int), robots))

