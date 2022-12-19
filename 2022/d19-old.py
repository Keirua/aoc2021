import heapq
import pprint
import re
from heapq import heappop, heappush

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


def compute_new_ressources(ressources, robots):
    return {k: robots[k] + ressources[k] for k in range(len(ressources_names))}
    # return {k: robots[k] + ressources.get(k, 0) for k in ressources_names}


def gen_successors(blueprint, ressources, robots):
    successors = []
    for ressource_name, costs in blueprint.items():
        idx = ressources_names.index(ressource_name)
        # If we have enough ressources to produce said robots, we can build one:
        if all([ressources[ressources_names.index(name)] > cost for cost, name in costs]):
            new_ressources = copy(ressources)
            new_robots = copy(robots)
            # new_ressources[name] += 1
            for cost, name in costs:
                new_ressources[idx] -= cost
            if ressource_name in new_robots:
                new_robots[idx] += 1
            else:
                new_robots[idx] = 1
            new_ressources = compute_new_ressources(new_ressources, robots)
            # New edge -> buying a new robot + extracting ressources
            successors.append((new_ressources, new_robots))
    # Then we can also dig for the ressources with the current robots
    new_ressources = compute_new_ressources(ressources, robots)
    successors.append((new_ressources, robots))
    return successors

from copy import copy
# import json
def dfs(blueprint, step, ressources, robots):
    Q = [(0, step, ressources, robots)]
    best_obsidian = 0
    while len(Q) > 0:
        nb_obsidian, step, ressources, robots = heapq.heappop(Q)
        if step == 0 and nb_obsidian > best_obsidian:
            best_obsidian = ressources[3]
            pp.pprint(ressources)
            # return ressources[3]
        else:
            for ressources, robots in gen_successors(blueprint, ressources, robots):
                # Q.append((ressources.get("obsidian", 0),  step-1, json.dumps(ressources), json.dumps(robots)))
                if step-1 > 0:
                    heapq.heappush(Q, (ressources[3],  step-1, ressources, robots))
    return best_obsidian


ressources_names = ["ore", "clay", "obsidian", "geode"]
text = open(f"d19.txt").read().strip()
text_sample = open(f"d19-sample.txt").read().strip()
# pp.pprint(parse(text))
# pp.pprint()
blueprints = parse(text_sample)
from collections import defaultdict
robots = defaultdict(int)
robots["ore"] = 1
# print(best_spend(blueprints[0], 24, defaultdict(int), robots))
print(dfs(blueprints[0], 24, (0, 0, 0, 0), (1, 0, 0, 0)))
