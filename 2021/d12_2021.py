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

from collections import defaultdict

def parse(input):
    edges = defaultdict(list)
    lines = input.split("\n")
    for line in lines:
        a, b = line.split("-")
        edges[a].append(b)
        edges[b].append(a)
    return edges


class Graph:
    def __init__(self, input):
        self.edges = parse(input)
        self.all_paths = []
        self.current_path = []
        self.visited = {k: False for k in self.edges.keys()}

    def dfs(self, u="start", v="end"):
        if u.islower() and self.visited[u]:
            return
        self.visited[u] = True
        self.current_path.append(u)
        if u == v:
            self.all_paths.append(self.current_path.copy())
            self.visited[u] = False
            self.current_path.pop()
            return
        for w in self.edges[u]:
            # print(self.edges[u])
            if (w.islower() and self.visited[w] == False) or w.isupper():
                self.dfs(w, v)
        self.current_path.pop()
        self.visited[u] = False

def part1(graph:Graph) -> int:
    graph.dfs()
    return len(graph.all_paths)

graph = Graph(input)
test_graph = Graph(test_input)
test_graph2 = Graph(test_input2)
test_graph3 = Graph(test_input3)
# test_graph.dfs("start", "end")
# pp.pprint(test_graph.all_paths)
assert(part1(test_graph) == 10)
assert(part1(test_graph2) == 19)
assert(part1(test_graph3) == 226)
print(part1(graph))
