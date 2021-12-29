
# Some cool links

## Some nice community links:

 - [Scatterplot of the resolution times](https://www.maurits.vdschee.nl/scatterplot/)
 - [A list of the nice problems since 2017](https://www.reddit.com/r/adventofcode/comments/kjuxkj/a_short_history_of_advent_problems_well_since/)
 - [a browser extension for extra stats in private leaderboards](https://github.com/jeroenheijmans/advent-of-code-charts)

## Cool external implementations

 - day 1: [implementation in Piet](https://www.reddit.com/r/adventofcode/comments/r6v23p/day_1_part_1_a_solution_in_piet_a_language_where/) (an esoteric, visual, stack-based language), explained a bit. 
 - day 3: [fun visualization with pygames](https://www.reddit.com/r/adventofcode/comments/r7x4yk/2021_day_3_part_2pygame_oxy_filter/)
 - day 4: [nice visualization with Love](https://www.reddit.com/r/adventofcode/comments/r8wq0c/2021_day_4_bingo_blinkenlights/)
 - [all of AoC 2021 in 17ms](https://www.reddit.com/r/adventofcode/comments/rozxsb/aoc_2021_highlyoptimized_solutions_in_rust_17ms/)

## Some cool other challenges I should complete
 - other non-finished years
 - CSES: https://cses.fi/problemset/ (worth going through https://www.geeksforgeeks.org/top-algorithms-and-data-structures-for-competitive-programming/, or similar like https://cp-algorithms.com/?)
 - https://www.reddit.com/r/adventofcode/comments/r99sio/where_to_find_other_programming_challenges/
 - cryptopals


## Todo (would be nice to dig a bit more)

Day 6 Upping the ante:
 - part3 googol:
   - [x] implement the matrix exponentiation solution
   - write an article about the process (naive implementation, linear time, then matrix exponentiation)
 - part4: 10^10^100: https://www.reddit.com/r/adventofcode/comments/ra88up/2021_day_6_part_4_day_googolplex/

day 5 upping the ante (maybe):
 - https://www.reddit.com/r/adventofcode/comments/r9zwj0/2021_day_5_unofficial_part_4_100000_long_vents/
 - https://www.reddit.com/r/adventofcode/comments/r9hpfs/2021_day_5_bigger_vents/hnf8obo/?context=3

day 7:
 - [x] implement the fast median and mean solutions
 - implement median in linear time: https://rcoh.me/posts/linear-time-median-finding/

day 8:
 - bruteforce the segments, in order to see if I can find the wire layout, à la J. Paulson: https://www.youtube.com/watch?v=DhQPrF-LBoE
 - write a cleaner version

day 9:
 - dfs is nice but union-find seems to be way faster: https://github.com/aldanor/aoc-2021/blob/f47999208d7ea2a6ffd3cfd5ad47e6188c0c3755/src/day09/mod.rs
 - 4 connected-component labelling: https://en.wikipedia.org/wiki/Connected-component_labeling

Day 15:
 - lookup how a priority queue is implemented
 - read about other cool graph algorithms:
   - ford-bellman (slower dijkstra that works on with negative weights: https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm)
   - graph coloring: https://en.wikipedia.org/wiki/Graph_coloring#Algorithms
   - minimum spanning tree (Prim, Kruskal)

Day 16:

Implement an utility BitArray class, with an API like bitstring:
```python
from bitstring import BitArray
bits = BitArray(hex='C200B40A82')
bits # BitArray('0xc200b40a82')
bits.bin #'1100001000000000101101000000101010000010'
bits[0:3] # BitArray('0b110')
bits[0:3].uint # 6
```

Day 21:
 - [x] write article about dynamic programming
 - solve more problems using DP (CSES?)
 - upping the ante:
   - reaching 1000:
     https://www.reddit.com/r/adventofcode/comments/rlgfyi/2021_day_21_part_3_playing_the_full_game/
     https://www.reddit.com/r/adventofcode/comments/rlm4p9/2021_day_21_part_3/

Read things about union/find







## Day 4

Quite happy with my (non-necessary) grid design that I’ve used in other problems already.
Grid display (modified from `display` on http://norvig.com/sudoku.html) is quite versatile:

```python
def __str__(self):
    """Display these values as a 2-D grid.
    Inspired by norvig’s sudoku: http://norvig.com/sudoku.html
    """
    width = 1 + max([len(str(self.lines[y][x])) for (x, y) in self.all_coords()])
    line = ""
    for l in self.lines:
        line += ''.join([str(c).center(width) for c in l]) + "\n"
    return line
```

## Day 5:

Wrote 3 different versions because I thought my code was incorrect. Turns out I typed the answer incorrectly.
The final version is O(N), the first is O(N^2) and is much slower.

Missed opportunity to dig Bresenham’s Line algorithm, but it wasn’t worth the effort

Harder:
 - https://www.reddit.com/r/adventofcode/comments/r9zwj0/2021_day_5_unofficial_part_4_100000_long_vents/
 - https://www.reddit.com/r/adventofcode/comments/r9hpfs/2021_day_5_bigger_vents/hnf8obo/?context=3

## Day 6

Like everybody I guess:
 - Initial implementation using a loooot of memory. O(exp(n)), ok-ish but already slow for n=80. Not suitable for second part (more than 1s/generation after n=180)
 - Much better implementation in O(n) using brain to think about the problem. Short, clean code, 0.37s up to n=150k

There is a generalization using matrix exponentation: https://old.reddit.com/r/adventofcode/comments/r9z49j/2021_day_6_solutions/hnfp9r9/
It has a log(n) implementation: https://www.geeksforgeeks.org/matrix-exponentiation/ or https://www.hackerearth.com/practice/notes/matrix-exponentiation-1/.
This approach might makes it possible to do the "upping the ante" part faster (n = 10k, n=150k), but the current solution is fast enough (0.37s)
Another approach is to find a generalization of the recurrence relation using a linear algebra package:
https://www.reddit.com/r/adventofcode/comments/ratue0/2021_day_6_fricas_solution_via_finding_a/

Todo: actually implement modular exponentiation for Upping the ante part3: 10^100
https://www.reddit.com/r/adventofcode/comments/ra3f5i/2021_day_6_part_3_day_googol/
Todo: Upping the ante part4: 10^10^100
https://www.reddit.com/r/adventofcode/comments/ra88up/2021_day_6_part_4_day_googolplex/

## Day 7

Went for a bruteforce approach, short and quick anyway.
[Someone explained](https://www.reddit.com/r/adventofcode/comments/rawxad/2021_day_7_part_2_i_wrote_a_paper_on_todays/) that part1 can be solved with the **median**, and part 2 around the **mean**.

More interestingly : it led me to discover that the **[median can be computed in O(n) time](https://rcoh.me/posts/linear-time-median-finding/)** using a variant of quicksort.

## Day 8 - 7-segment display

My implementation sucked.
 - a simple(r, slightly) solution [explained visually](https://www.reddit.com/r/adventofcode/comments/rbvpui/2021_day_8_part_2_my_logic_on_paper_i_used_python/)
 - a clever solution involves bitmasks: https://www.reddit.com/r/adventofcode/comments/rc5s3z/comment/hntdb91/?utm_source=share&utm_medium=web2x&context=3
 - 2 nice approaches from [Jonathan Paulson](https://www.youtube.com/watch?v=DhQPrF-LBoE)
    - bruteforcing the segment values. Slow (40s), but fast to code. Todo: code this approach?
    - identifying the segment values with logic. Fast (0.3s) but slow to code ;). Much cleaner than mine

## Day 9

It was cool to implement [floodfilling](https://en.wikipedia.org/wiki/Flood_fill#Moving_the_recursion_into_a_data_structure), and to be able to implement it without looking at pseudocode.

```python
from collections import deque
def find_basin(grid, start):
    """Find the basin that contains the starting position using flood filling"""
    basin = [start]
    visited = [start]
    queue = deque(grid.neighbours4(start[0], start[1]))
    while len(queue) > 0:
        t = queue.popleft()
        if grid.get(t[0], t[1]) != 9 and t not in visited:
            basin.append(t)
            visited.append(t)

            for n in grid.neighbours4(t[0], t[1]):
                queue.append(n)

    return basin
```


# Day 12:
 - my own implementation for part 1 (recursive DFS)
 - read about how to make an iterative DFS for part2 here:
   https://github.com/mebeim/aoc/blob/master/2021/README.md#day-12---passage-pathing
   also worth reading: https://github.com/hyper-neutrino/advent-of-code/blob/main/2021/day12p1.py

# day 15: dijkstra \o/

My grid class was useful again

```python
import heapq
def dijkstra_fast(grid:Grid, start=(0, 0), end=None):
    """faster dijkstra implementation using a priority queue"""
    dist = { v: 1000000000000000 for v in grid.all_coords()}
    dist[start] = 0
    prev = { v: None for v in grid.all_coords() }
    Q = [(0, start)]
    while len(Q) > 0:
        min_dist, min_u = heapq.heappop(Q)
        # we may provide an end node, if so we can break early
        if end is not None and min_u == end:
            break
        if min_dist > dist[min_u]:
            continue

        for v in grid.neighbours4(min_u):
            alt = min_dist + int(grid[v])
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = min_u
                heapq.heappush(Q, (alt, v))

    return dist, prev
```
   
# day 21

part2 was a nice dynamic programming problem, quite happy with my solution

# Day 22

 - using coordinate compression
 - seems to be a [clique finding problem](https://en.wikipedia.org/wiki/Clique_problem) ?
   - Bron–Kerbosch_algorithm: https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm

# day 24

 - wrote an article on the topic that summarizes many approaches

# day 25

 - the [BML traffic model](https://en.wikipedia.org/wiki/Biham%E2%80%93Middleton%E2%80%93Levine_traffic_model)