
# Day 2

Was boring until orlp explain his technique:
 - https://www.reddit.com/r/adventofcode/comments/zpihwi/comment/j0w57ob/?utm_source=share&utm_medium=web2x&context=3
 - https://github.com/orlp/aoc2022/blob/master/src/bin/day02.rs

# Day 6

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

# day 9

I love the pattern of using regexes and one-liners for parsing:

```python
moves = [(dir, int(dist)) for (dir, dist) in re.findall(r"([RDLU]) (\d+)", input)]
```
# day 11:

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


# day 12: dijkstra

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

# day 13: sorting according to a custom function

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

# Day 14:

Fun automaton, many nice visualizations on reddit.

# Day 15:

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
 
## Day 19

BFS + memoization + search tree pruning for me (30s for both parts!…)

Branch-and-bound best-first search over the choices of which robot to build seems much better
https://www.reddit.com/r/adventofcode/comments/zpihwi/comment/j0vvzgz/?utm_source=share&utm_medium=web2x&context=3