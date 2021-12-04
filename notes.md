# 2015 day 7

Different ideas for solving this problem:

 - mine: classic parsing & execution of the language by recursively compute dependency the tree, starting from the goal 
 - use regex to reformat and sort the code (?!), then run eval
 - use regex to write a large recursive solver: https://gist.github.com/mgiuffrida/f275912b9bd92a3f403e
 - use Z3 to solve the tree https://mobeigi.com/blog/capture-the-flag/advent-of-code/advent-of-code-day-7/

# 2015 day 10
There was an interesting construct, where you have to implement a sequence
of the form `n = f(n)`, then call it many times:

```python
def look_and_say(input, nb_iterations=40):
    n = input
    for _ in range(nb_iterations):
        n = next_it(n)
    return len(n)
```

`next_it` implements the [Look-and-say sequence](https://en.wikipedia.org/wiki/Look-and-say_sequence).

It can be done with `itertools` too:
```python
from itertools import accumulate
def look_and_say(input, nb_iterations=40):
    l = lambda a, b: next_it(a)
    iterations = accumulate(range(nb_iterations), l, initial=input)
    return len(list(iterations)[-1])
```
Since our function `next_it` only takes one parameter, we have to introduce
a lambda with 2 parameters and not use the second one.

The problem is that `accumulate` return an iterator over all the values,
while we are  only interested in the last one.

A better solution is to use `functools.reduce`: 

```python
from functools import reduce
def look_and_say(input, nb_iterations=40):
    # we need to introduce a lambda
    l = lambda a, b: next_it(a)
    final_value = reduce(l, range(nb_iterations), input)
    return len(final_value)
```


# 2021

 - day 1: implementation in Piet (an esoteric, visual, stack-based language), explained a bit: https://www.reddit.com/r/adventofcode/comments/r6v23p/day_1_part_1_a_solution_in_piet_a_language_where/
 - day 3: fun visualization with pygames: https://www.reddit.com/r/adventofcode/comments/r7x4yk/2021_day_3_part_2pygame_oxy_filter/

## Day 4

Quite happy with my (non-necessary) grid design that I’ve used in other problems already.
Grid display (modified from `display` on http://norvig.com/sudoku.html) is quite versatile