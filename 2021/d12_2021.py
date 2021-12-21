from aoc import input_as_string, challenge_filename
import re, pprint, itertools as it

pp = pprint.PrettyPrinter(indent=4)

input = input_as_string(challenge_filename(12, 2021))
test_input = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""
test_input2 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

test_input3 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""

from collections import defaultdict, deque


def parse(input):
    edges = defaultdict(list)
    lines = input.split("\n")
    for line in lines:
        a, b = line.strip().split("-")
        if b != "start":
            edges[a].append(b)
        if a != "start":
            edges[b].append(a)
    return edges


class Graph:
    def __init__(self, input):
        self.edges = parse(input)
        self.reset()

    def reset(self):
        self.all_paths = []
        self.current_path = []
        self.visited = {k: 0 for k in self.edges.keys()}

    def dfs(self, u="start", v="end"):
        if u.islower() and self.visited[u] == 1:
            return
        self.visited[u] = 1
        self.current_path.append(u)
        if u == v:
            self.all_paths.append(self.current_path.copy())
            self.visited[u] = 0
            self.current_path.pop()
            return
        for w in self.edges[u]:
            if (w.islower() and self.visited[w] == 0) or w.isupper():
                self.dfs(w, v)
        self.current_path.pop()
        self.visited[u] = 0

    def dfs2(self, u="start", v="end"):
        queue = deque([(u, set([u]), False)])
        nb_paths = 0
        while queue:
            n, visited, twice = queue.pop()
            if n == v:
                nb_paths += 1
                continue
            for w in self.edges[n]:
                if w not in visited or w.isupper():
                    queue.append((w, visited | set([w]), twice))
                    continue
                # w must be lowercase and already visited. No need to add it to the visited set
                # and set twice to true
                if twice:
                    continue

                queue.append((w, visited, True))

        return nb_paths


def part1(graph: Graph) -> int:
    graph.reset()
    graph.dfs()
    return len(graph.all_paths)


def part2(graph: Graph) -> int:
    graph.reset()
    return graph.dfs2()
    # for p in graph.all_paths:
    #     print(",".join(p))


graph = Graph(input)
test_graph = Graph(test_input)
pp.pprint(test_graph.edges)
test_graph2 = Graph(test_input2)
test_graph3 = Graph(test_input3)
# test_graph.dfs("start", "end")
# pp.pprint(test_graph.all_paths)
assert (part1(test_graph) == 10)
assert (part1(test_graph2) == 19)
assert (part1(test_graph3) == 226)
print(part1(graph))
assert (part2(test_graph) == 36)
print(part2(graph))
# assert(part2(test_graph2) == 103)
# assert(part2(test_graph3) == 3509)
