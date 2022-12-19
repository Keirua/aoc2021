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
            blueprint[w[3]] = parse_costs(costs[0][1:])
            blueprint[w[9]] = parse_costs(costs[1][1:])
            blueprint[w[15]] = [parse_costs(costs[2][1:]), parse_costs(costs[3][1:])]
            blueprint[w[24]] = [parse_costs(costs[4][1:]), parse_costs(costs[5][1:])]

            # print(line)
            # print(costs)
            # pp.pprint(blueprint)
            out.append(blueprint)
    return out

ressources = ["ore", "clay", "obsidian", "geode"]

text = open(f"d19.txt").read().strip()
text_sample = open(f"d19-sample.txt").read().strip()
# pp.pprint(parse(text))
pp.pprint(parse(text_sample))


# pp.pprint(blueprints)
