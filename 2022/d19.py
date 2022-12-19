import pprint as pp
import re
from collections import deque


def parse(text):
    # Blueprint 1:
    #   Each ore robot costs 4 ore.
    #   Each clay robot costs 4 ore.
    #   Each obsidian robot costs 4 ore and 14 clay.
    #   Each geode robot costs 2 ore and 16 obsidian.
    #
    # idx, ore_cost, clay_cost, obsidian_cost_in_ore, obsidian_cost_in_clay, geode_cost_in_ore, geode_cost_in_obsidian
    # idx, o, c, ob_ore, ob_clay, g_ore, g_obsidian
    return [list(map(int, re.findall("(\d+)", line))) for line in text.split("\n")]


def solve(o: int, c: int, ob_ore: int, ob_clay: int, g_ore: int, g_obsidian: int, T: int) -> int:
    """
    DFS with memoization. Need to explore the entire search space so pretty slow
    """
    # How many ressources we have, and how many of each ressources we have
    # at first: 0 ressources, and 1 robot for ore
    Q = deque([(0, 0, 0, 0, 1, 0, 0, 0, T)])
    max_nb_geodes = 0
    SEEN = set()
    max_ore_required = max([o, c, ob_ore, g_ore])
    while len(Q) > 0:
        no, nc, nob, ng, ro, rc, rob, rg, t = Q.popleft()
        max_nb_geodes = max(max_nb_geodes, ng)
        # if len(SEEN) % 100_000 == 0:
        #     print(len(SEEN), max_nb_geodes, t)
        if t == 0:
            continue

        S = (no, nc, nob, ng, ro, rc, rob, rg, t)
        if S in SEEN:
            continue
        SEEN.add(S)

        # If we have the resources, we build a new robot
        if no >= o:  # ore
            Q.append((no - o + ro, nc + rc, nob + rob, ng + rg, ro + 1, rc, rob, rg, t - 1))
        if no >= c:  # clay
            Q.append((no - c + ro, nc + rc, nob + rob, ng + rg, ro, rc + 1, rob, rg, t - 1))
        if no >= ob_ore and nc >= ob_clay:  # obsidian
            Q.append((no - ob_ore + ro, nc - ob_clay + rc, nob + rob, ng + rg, ro, rc, rob + 1, rg, t - 1))
        if no >= g_ore and nob >= g_obsidian:  # do we have the ressources to build geodes robots?
            Q.append((no - g_ore + ro, nc + rc, nob - g_obsidian + rob, ng + rg, ro, rc, rob, rg + 1, t - 1))
        # Extract resources with the existing robots, but do not build a new robot
        Q.append((no + ro, nc + rc, nob + rob, ng + rg, ro, rc, rob, rg, t - 1))
    return max_nb_geodes


text = open(f"d19.txt").read().strip()
text_sample = open(f"d19-sample.txt").read().strip()

blueprints = parse(text_sample)
part1 = 0
for idx, o, c, ob_ore, ob_clay, g_ore, g_obsidian in blueprints:
    print(idx, o, c, ob_ore, ob_clay, g_ore, g_obsidian)
    max_g = solve(o, c, ob_ore, ob_clay, g_ore, g_obsidian, 24)
    print(idx, max_g)
    part1 += idx * max_g
print(part1)