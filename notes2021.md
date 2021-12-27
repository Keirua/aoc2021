
# 2021

Scatterplot per resolution time:
https://www.maurits.vdschee.nl/scatterplot/

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
 - see if I can implement it with Z3

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
 - write article about dynamic programming
 - solve more problems using DP (CSES?)
 - upping the ante:
   - reaching 1000:
     https://www.reddit.com/r/adventofcode/comments/rlgfyi/2021_day_21_part_3_playing_the_full_game/
     https://www.reddit.com/r/adventofcode/comments/rlm4p9/2021_day_21_part_3/

Read things about union/find



## Some cool other challenges I should complete:
 - other non-finished years
 - CSES: https://cses.fi/problemset/ (worth going through https://www.geeksforgeeks.org/top-algorithms-and-data-structures-for-competitive-programming/, or similar like https://cp-algorithms.com/?)
 - https://www.reddit.com/r/adventofcode/comments/r99sio/where_to_find_other_programming_challenges/
 - cryptopals

## Cool external implementations

 - day 1: implementation in Piet (an esoteric, visual, stack-based language), explained a bit: https://www.reddit.com/r/adventofcode/comments/r6v23p/day_1_part_1_a_solution_in_piet_a_language_where/
 - day 3: fun visualization with pygames: https://www.reddit.com/r/adventofcode/comments/r7x4yk/2021_day_3_part_2pygame_oxy_filter/
 - day 4: nice visualization with Love: https://www.reddit.com/r/adventofcode/comments/r8wq0c/2021_day_4_bingo_blinkenlights/

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
A solution involving the median for part1 works (and mean for part2):
 - proof: https://www.reddit.com/r/adventofcode/comments/rawxad/2021_day_7_part_2_i_wrote_a_paper_on_todays/
 - not very mathematical talk: https://www.reddit.com/r/adventofcode/comments/rar7ty/2021_day_7_solutions/hnkd58g/?utm_source=share&utm_medium=web2x&context=3
More interestingly: median can be computed in O(n) time:
https://rcoh.me/posts/linear-time-median-finding/

## Day 8 - 7-segment display

My implementation sucked.
 - it might be a good exercise to revisit it with Z3 (https://www.reddit.com/r/adventofcode/comments/rbwnh5/2021_day_8_can_it_be_solved_as_a_constraint/)
 - a simple(r, slightly) solution explained visually: https://www.reddit.com/r/adventofcode/comments/rbvpui/2021_day_8_part_2_my_logic_on_paper_i_used_python/
 - a clever solution involves bitmasks: https://www.reddit.com/r/adventofcode/comments/rc5s3z/comment/hntdb91/?utm_source=share&utm_medium=web2x&context=3
 - 2 nice approaches from Jonathan Paulson: https://www.youtube.com/watch?v=DhQPrF-LBoE
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

# day 10: token parsing (validation of the structure of ()<>[]{} and completion)
# day 11: cellular automaton. Cool to reuse my grid class

# Day 12:
 - my own implementation for part 1 (recursive DFS)
 - read about how to make an iterative DFS for part2 here:
   https://github.com/mebeim/aoc/blob/master/2021/README.md#day-12---passage-pathing
   also worth reading: https://github.com/hyper-neutrino/advent-of-code/blob/main/2021/day12p1.py



# day 15: dijkstra \o/
my grid class was useful again
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

# day 17
A simple mechanic speed/acceleration problem
Of course it has an analytical solution:
 - https://www.reddit.com/r/adventofcode/comments/ri9kdq/2021_day_17_solutions/hoxa0vi/?utm_source=reddit&utm_medium=web2x&context=3
 - https://github.com/mebeim/aoc/blob/master/2021/README.md#day-17---trick-shot
but writing code was faster that early
   
# day 21

part2 was a nice dynamic programming problem, quite happy with my solution

# day 24

 - reverse engineering the ALU program:
https://topaz.github.io/paste/#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
 - solving the problem using symbolic calculation:
https://www.reddit.com/r/adventofcode/comments/rnwz9p/2021_day_24_solving_the_alu_programmatically_with/