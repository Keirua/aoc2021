
# Cool stuff

## links
AoC stats:
https://jeroenheijmans.github.io/advent-of-code-surveys/
CSES: many problems https://cses.fi/problemset/

Summary of some cool algorithms & data structures:
Graph traversal:
 - bfs/dfs: https://medium.com/nerd-for-tech/dfs-bfs-introduction-26a65fca2344
 - dijkstra & bellman ford: https://blog.devgenius.io/shortest-path-algorithms-dijkstra-bellman-ford-3b640bdb0449
 - floyd warshall: https://blog.devgenius.io/shortest-path-algorithm-floyd-warshall-johnsons-632fd7a9f8c7
Various optimization:
 - Union Find: https://python.plainenglish.io/union-find-data-structure-in-python-8e55369e2a4f
 - branch and bound: https://en.wikipedia.org/wiki/Branch_and_bound
 - simulated annealing: http://katrinaeg.com/simulated-annealing.html

## Stuff I learnt

 - frozenset = set + immutable + hashable. So it can be used as a key
 - `set` can be implemented with bit operations
 - dijkstra, bfs/dfs, floodfill
 - stdlib:
   - heapq
   - deque
   - multiprocessing
   - `from operator import add, sub, mul, floordiv`
 - regexes:
   - using backreferences (day21)?
   - re.findall, re.split
 - algos:
   - binary operations (^ = not all, popcount) 
   - topological sort
   - graph simplification (floyd warshall)
   - Constraint solvers. z3, but there cpmpy uses MIP (mixed integer programming) and seems powerfull
   - using heuristics to prune the search space (branch and bound)

## Day 2

Was boring until orlp explain his technique:
 - https://www.reddit.com/r/adventofcode/comments/zpihwi/comment/j0w57ob/?utm_source=share&utm_medium=web2x&context=3
 - https://github.com/orlp/aoc2022/blob/master/src/bin/day02.rs

## Day 6

The naive solution is O(n*window_size), but interestingly, it can be solved in O(n) with [a bit trick](https://www.mattkeeter.com/blog/2022-12-10-xor/)

Totally unnecessary since n = 4096 and window_size is {4, 14}, but clever anyway.

```python
# First, we convert our naive solution using sets into binary ORs:
def solve_or(input:str, N:int) -> int:
    for i in range(len(input)-N):
        s = 0
        for j in range(N):
            # ord(input[i + j]) - ord('a') => turn input letters a-z into 0-26
            # 1 << (ord(input[i + j]) - ord('a')) = 2 ** (letter position)
            # s |= b0001 -> sets bit 0001 in s
            s |= 1 << (ord(input[i + j]) - ord('a'))
        if bin(s).count("1") == N: # there was no native popcnt in python until 3.10
            return i + N

# but we want to remove the N loop. We use the fact that a ^ b ^ a == b
def solve(input:str, N:int) -> int:
    s = 0
    for i in range(len(input)):
        # Turn on bits as they enter the window
        s ^= 1 << (ord(input[i]) - ord('a'))
        if i >= N:
            # Turn bits off as we leave the window
            s ^= 1 << (ord(input[i - N]) - ord('a'))
        if s.bit_count() == N:
            return i + 1
```

Led to some interesting reading: https://stackoverflow.com/questions/109023/count-the-number-of-set-bits-in-a-32-bit-integer#109025

## day 9

I love the pattern of using regexes and one-liners for parsing:

```python
moves = [(dir, int(dist)) for (dir, dist) in re.findall(r"([RDLU]) (\d+)", input)]
```
## day 11:

regex + lambda + eval for the parsing

```python
import re
operation_code = re.search(r"new = (.*)", lines[2]).group(1)
return cls(
    items=Counter([int(s) for s in re.findall("(\d+)", lines[1])]),
    operation_code=operation_code,
    op=lambda old: eval(operation_code),
    test=int(lines[3].split()[-1]),
    on_true=int(lines[4].split()[-1]),
    on_false=int(lines[5].split()[-1])
)
```


## day 12: dijkstra

Dijkstra with an heapq for faster search, then dijkstra with multiple starting point.

```python
import heapq
def dijkstra(grid, start=(0, 0), end=None):
    """Dijkstra's algorithm implementation using a priority queue"""
    # Initial state:
    #  - all the distances to the starting node are maximal
    #    (except the starting node: it has a distance of 0 to itself).
    #  - all the ancestors are non-existing
    dist = { v: 1000000000000000 for v in grid.all_coords()}
    dist[start] = 0
    prev = {v: None for v in grid.all_coords()}

    # The queue of nodes we will consider, with one starting point:
    Q = [(0, start)]
    while len(Q) > 0:
        # We consider the "cheapest" node, that is the node with the lowest cost.
        # We store the tuples (cost, position). In this context, heapq.heappop compares on the cost
        # https://docs.python.org/3.11/library/heapq.html#basic-examples
        min_dist, min_coord = heapq.heappop(Q)

        # we may provide an end node, if so we can break early
        if end is not None and min_coord == end:
            break

        if min_dist > dist[min_coord]:
            continue

        for neighbour in grid.valid_neighbours(min_coord):
            new_distance = min_dist + 1
            # If we found a better path, we update both the cost and the predecessor
            # and add this node to the queue
            if new_distance < dist[neighbour]:
                dist[neighbour] = new_distance
                prev[neighbour] = min_coord
                heapq.heappush(Q, (new_distance, neighbour))

    return dist, prev
```

## day 13: sorting according to a custom function

I cheated and parsed with `eval`. My comparison function cannot be used in `sorted` directly:

```python
def cmp(a, b):
    # do something
    return -1, 0 or 1

sorted_packets = sorted(packets, key=functools.cmp_to_key(cmp))
p2 = (sorted_packets.index([[2]])+1) * (sorted_packets.index([[6]])+1)
print(p2)
```

[mjpieters](https://github.com/mjpieters/adventofcode/blob/master/2022/Day%2013.ipynb) is way more idiomatic:
 - he made a custom parser, kudos to him
 - he implemented `__lt__` in order to use `sort` natively

## Day 14:

Fun automaton, many nice visualizations on reddit.

## Day 15:

From part2 it was pretty clear that a bruteforce solution wouldn’t work fast, or fast enough with what I had.
It was pretty cool (though overkill probably ;)) to use z3 to solve part 2

```python
def part2(positions, xy_max):
    solver = Solver()
    tx, ty, p2 = Ints("x y p2")
    solver.add(And(tx >= 0, tx <= xy_max))
    solver.add(And(ty >= 0, ty <= xy_max))
    solver.add(p2 == tx*4000000+ty)
    for (x, y, x2, y2) in positions:
        dist = manhattan_distance(x, y, x2, y2)
        solver.add(z3Abs(x-tx)+z3Abs(y - ty) > dist)
    solver.check()
    m = solver.model()
    return m[p2]
```

I later found out (https://www.youtube.com/watch?v=OG1QwJ2RKsU) an elegant algo to merge the intervals for part 1. It
reduces the memory footprint and it’s much faster than using set operations.

```python
# Say we have the following intervals, a list of [a,b)
intervals = [[9,10],[9,15],[10,12],[-1,0], [9,10],[2,4],[2,3],[1,3],[6,8]]

def merge_intervals(intervals):
    intervals.sort()
    stack = [intervals[0]]
    for lo, hi in intervals[1:]:
        qlo, qhi = stack[-1]
        # We can play with <= and <= 1+ in order to change how we represent those ranges,
        # depending on if the upper value is included or not
        if lo <= qhi:
            # The new interval overlaps the largest, latest range, so we update the max
            stack[-1][1] = max(hi, qhi)
        else:
            stack.append([lo, hi])
    return stack

# output:
# [[-1, 0], [1, 4], [6, 8], [9, 15]]
stack = merge(intervals)
print(stack)
```

## Day 16

bitfield -> hash the combination names
dynamic programming
Graph simplification? -> https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
DFS ?

MIP: Mixed Integer programming
https://www.reddit.com/r/adventofcode/comments/zn6k1l/comment/j0g8ejd/?utm_source=reddit&utm_medium=web2x&context=3
https://www.youtube.com/watch?v=A4mmmDAdusQ

## Day 18

 -> floodfill for part 2
Extracted the bounding box, then made a floodfill to find the outer shell. From that, I could deduce the inner shell
I tried adding my custom set using integer bit operations, but this was (a bit surprisingly) slower

 -> jonathan paulson did this in reverse:
    - he made a floodfill
    - if the floodfill lasted forever, he’d conclude the point is on the outside
    - then he used memoization to give a x100 speed boost

Maybe a usecase for unionfind? https://python.plainenglish.io/union-find-data-structure-in-python-8e55369e2a4f
 
## Day 19

BFS + memoization + search tree pruning for me + multiprocessing (18s for both parts!…)

```python
from multiprocessing import Process, Queue
def solve_mp(queue, blueprint, t):
    idx, o, c, ob_ore, ob_clay, g_ore, g_obsidian = blueprint
    nb_geodes = solve(o, c, ob_ore, ob_clay, g_ore, g_obsidian, t)
    queue.put((idx, nb_geodes))

def p1_mp(blueprints):
    queue = Queue()
    procs = []
    for line in blueprints:
        proc = Process(target=solve_mp, args=(queue, line, 24))
        proc.start()
        procs.append((proc, queue))
    total = 0
    for p, q in procs:
        p.join()  # this blocks until the process terminates
        idx, nb_geodes = q.get()
        total += idx*nb_geodes
    return total
```

Branch-and-bound best-first search over the choices of which robot to build seems much better
https://www.reddit.com/r/adventofcode/comments/zpihwi/comment/j0vvzgz/?utm_source=share&utm_medium=web2x&context=3

## Day 20

Quite easy with a [`collections.deque`](https://docs.python.org/3/library/collections.html#collections.deque).

## Day 21

Easy but nice. Part 1 = simple tree traversal. Part 2 with z3. There was a nice hack with eval too.


I could have used the standard library instead of writing my own lambdas: 
```python
from operator import add, sub, mul, floordiv
operations = {'-': sub, '+': add, '/': floordiv, '*': mul}
```
I found two nice solutions:


 - reversing the tree to isolate the variable, then solve (TODO: implement this)
https://topaz.github.io/paste/#XQAAAQArBwAAAAAAAAAzHIoib6qZzo2OBd79LRjVLyEQ+mpAR5Uve8TJXQOY6DLfIpGeBRXQbJHs0UDBBvpxKQMLLLiWoNdX9S3YkBL5RwN25jUGDuD1SWEasASDHwIkif2uPp6YIwXf2sK/YXD6X+eeD/aYr70551yXVFu3Sbw7VHlmMFE4N+/7HhoDDwtkJsnzLIJBpvelIfDNGxpbYzV+FR3ztABqpyv05mIKcyVOG2lQhAIETykXSmnbF6M7MNxvXS3VGQoXDifWMQD4DdfITposOwBJ1RHFgVLM0QsENGxooJo0MANmFLW5j9z4L/1tRbgadbCLst+TRyeI81E9u1bgW/LEF6QSOUtPBz4nQfDvNhHPwjwWJYX/xA6sCzfaX1A9HL4ACeUxhrSwKDk+rsBJTo6mzo2sDenXU0N0309ICFxDN4ZdMaQ5hZjVcyr559zcB71kHWMwfb4utpMM2+Lz3cUgXOVL0K9TNH1FqXnwuD7VGPaye/13mf6mi96o0cTi70QKhKhdez4p/8CnYw4sqp9Ac3y4gjjMi91j65NStIWznp89j+9oO/+j6Mjce9y02msal3GsLRRVrxml9i3cRXizVcZVo8zduWDPw7muB4IW4H1/6trQdeMbQpkhLIvxyr1t5zVgMf9Beg1yUI/TKr8BckGDVVFbuX5jCT8seDVqNmU37V0kSi7otXkZjJDtpeE6kgcxj0w9N2jUdg4lDGDnOgeCpy1ylhzA10arxelBs/+hNrOkp6l8sJkMpgIRmGQpK9YLeRJcWWIT58gCtdvNroh4VcNHuySNbwjRUt+Ydy2jw2P3p8f+Z0nFmhA1z8z4xlI5o3ZerQxDMZ69v8WL+35XMshQsxUiXNKjRvnySqiCPwNcrmHIeRDwNzqmU8Ek/B14c7TfCfnl1LIRpHE0kQYh//Y+Ipw=
 - replace human with 1j (the complex number) so that python deal with numbers on its own.
Works because it’s used only once, not 2 multiplications by human
Then either user a solver by replacing the imaginary part, or solve as is.
https://www.reddit.com/r/adventofcode/comments/zrav4h/comment/j133ko6/
