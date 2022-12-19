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
    BFS with memoization. Need to explore the entire search space so pretty slow
    """
    # How many resources we have, and how many of each resources we have
    # at first: 0 resources, and 1 robot for ore
    Q = deque([(0, 0, 0, 0, 1, 0, 0, 0, T)])
    max_nb_geodes = 0
    SEEN = set()
    max_ore_required = max([o, c, ob_ore, g_ore])
    while len(Q) > 0:
        no, nc, nob, ng, ro, rc, rob, rg, t = Q.popleft()
        max_nb_geodes = max(max_nb_geodes, ng)

        if t == 0:
            continue

        # Do not produce more resources or robots than necessary
        ro = min(ro, max_ore_required)
        rc = min(rc, ob_clay)
        rob = min(rob, g_obsidian)
        no = min(no, t * max_ore_required - ro * (t - 1))
        nc = min(nc, t * ob_clay - rc * (t - 1))
        nob = min(nob, t * g_obsidian - rob * (t - 1))
        # thus, we can feed the memoization with already seen states
        S = (no, nc, nob, ng, ro, rc, rob, rg, t)
        if S in SEEN:
            continue
        SEEN.add(S)

        # If we have the resources, we build a new robot
        if no >= o:  # ore robot
            Q.append((no - o + ro, nc + rc, nob + rob, ng + rg, ro + 1, rc, rob, rg, t - 1))
        if no >= c:  # clay robot
            Q.append((no - c + ro, nc + rc, nob + rob, ng + rg, ro, rc + 1, rob, rg, t - 1))
        if no >= ob_ore and nc >= ob_clay:  # obsidian robot
            Q.append((no - ob_ore + ro, nc - ob_clay + rc, nob + rob, ng + rg, ro, rc, rob + 1, rg, t - 1))
        if no >= g_ore and nob >= g_obsidian:  # geode robots
            Q.append((no - g_ore + ro, nc + rc, nob - g_obsidian + rob, ng + rg, ro, rc, rob, rg + 1, t - 1))
        # Extract resources with the existing robots, but do not build a new robot
        Q.append((no + ro, nc + rc, nob + rob, ng + rg, ro, rc, rob, rg, t - 1))
    return max_nb_geodes


text = open(f"d19.txt").read().strip()

blueprints = parse(text)
part1 = 0
part2 = 1
for idx, o, c, ob_ore, ob_clay, g_ore, g_obsidian in blueprints:
    # part1 += idx * rint(idx, o, c, ob_ore, ob_clay, g_ore, g_obsidian)
    if idx <= 3:
        part2 *= solve(o, c, ob_ore, ob_clay, g_ore, g_obsidian, 32)
print(part1)
print(part2)