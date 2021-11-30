from collections import deque

edges = {
    "a": ["b", "c"], # from a, it is possible to go to b or c
    "b": ["d", "e"],
    "c": ["f", "g"],
    "d": [],
    "e": ["h"],
    "f": [],
    "g": []
}

# Sample code from
# https://en.wikipedia.org/wiki/Breadth-first_search#Pseudocode
# Is it possible to go from root to goal ?
def bfs(G, root, goal):
    Q = deque()
    SEEN = [root]
    Q.appendleft(root)
    while not len(Q) == 0:
        v = Q.popleft()
        if v == goal:
            return True
        if v in G:
            for w in G[v]: # for all neighbor vertices w of v
                if w not in SEEN:
                    SEEN.append(w)
                    Q.appendleft(w)
    return False

# iterative DFS:
# https://en.wikipedia.org/wiki/Depth-first_search#Pseudocode
def dfs(G, root, goal):
    S = [root]
    SEEN = []
    while len(S) > 0:
        v = S.pop()
        if v == goal:
            return True
        if v in G and v not in SEEN:
            SEEN.append(v)
            for w in G[v]: # for all neighbor vertices w of v
                S.append(w)
    return False


print(bfs(edges, "a", "h"))
print(bfs(edges, "a", "c"))
print(bfs(edges, "b", "c"))

print(dfs(edges, "a", "h"))
print(dfs(edges, "a", "c"))
print(dfs(edges, "b", "c"))