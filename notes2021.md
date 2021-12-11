
# 2021

## Todo (would be nice to dig a bit more)

Day 6 Upping the ante:
 - part3 googol: write an article about the process (naive implementation, linear time, then matrix exponentiation)
 - part4: 10^10^100: https://www.reddit.com/r/adventofcode/comments/ra88up/2021_day_6_part_4_day_googolplex/

day 5 upping the ante (maybe):
 - https://www.reddit.com/r/adventofcode/comments/r9zwj0/2021_day_5_unofficial_part_4_100000_long_vents/
 - https://www.reddit.com/r/adventofcode/comments/r9hpfs/2021_day_5_bigger_vents/hnf8obo/?context=3

day 7: implement median in linear time:
 - https://rcoh.me/posts/linear-time-median-finding/

day 8:
 - bruteforce the segments, in order to see if I can find the wire layout, à la J. Paulson: https://www.youtube.com/watch?v=DhQPrF-LBoE
 - write a cleaner version
 - see if I can implement it with Z3

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
Apparently a solution involving the median for part1 works (and mean for part2):
proof: https://www.reddit.com/r/adventofcode/comments/rawxad/2021_day_7_part_2_i_wrote_a_paper_on_todays/
not very mathematical talk: https://www.reddit.com/r/adventofcode/comments/rar7ty/2021_day_7_solutions/hnkd58g/?utm_source=share&utm_medium=web2x&context=3
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