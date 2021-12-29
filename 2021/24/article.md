
I had a blast working through the problem 24 of AdventOfCode 2021. The size of the input (9^14 possibilities) forced us
to get rid of the brute force idea and try many things.
Reverse engineering a program in a custom language was fun, using Z3 is always cool, and many people were very creative.

There are many ways to think about this problem, and after being stuck for a while, I spent some time on the
subreddit understanding the different approaches and rewriting different solutions myself.

Here is a breakdown of some approaches that resonated with me ; they are conceptually very different.

I’ve studied ad hoc solutions (solutions tailor-made for this particular ALU program) and generic solutions (solutions that could work for any ALU program).

 - Ad hoc solutions
   - Understanding the ALU program
   - Bottom-up resolution
   - Top-down, stack/base 26 approach
   - Using Z3 to solve the simplified subroutines
   - The hacker way: using GCC to simplify the equations, then using Z3
 - Generic solutions
   - Clever bruteforcing
   - Semi generic: DFS with memoization
   - Using Z3 to encode the entire ALU program as a set of constraints
   - Custom symbolic simplification

# Problem statement

[Advent of Code 2021 Day 24 is described here](https://adventofcode.com/2021/day/24). Here is a summary:

You are given an ALU program, that consist of 252 instructions.
14 inputs values, whose values all are between 1 and 9.
It has integer variables w, x, y, and z. These variables all start with the value 0.
The ALU also supports six instructions:

 - inp a - Read an input value and write it to variable a.
 - add a b - Add the value of a to the value of b, then store the result in variable a.
 - mul a b - Multiply the value of a by the value of b, then store the result in variable a.
 - div a b - Divide the value of a by the value of b, truncate the result to an integer, then store the result in variable a. (Here, "truncate" means to round the value toward zero.)
 - mod a b - Divide the value of a by the value of b, then store the remainder in variable a. (This is also called the modulo operation.)
 - eql a b - If the value of a and b are equal, then store the value 1 in variable a. Otherwise, store the value 0 in variable a.

In all of these instructions, a and b are placeholders; a will always be the variable where the result of the operation is stored (one of w, x, y, or z), while b can be either a variable or a number. Numbers can be positive or negative, but will always be integers.

What is the highest input so that register z=0 at the end of the program ?

# Ad hoc solutions

In this first part, we’ll take a look at the solutions where people reverse-engineered the ALU program and used some of its properties
to solve the problem.

## Understanding the ALU program

The ALU program we need to study has 14 times the same 18-instruction program. Only 3 elements will vary:

```bash
inp w
mul x 0
add x z
mod x 26
div z 1  -> this value can change
add x 11 -> this value can change
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 16 -> this value can change
mul y x
add z y
```

During the remainder of this article, we’ll give the same name to those parameters:
 - on line 4: `zdiv`
 - on line 5: `xcheck`
 - on line 15: `yadd`

We can first write a piece of code in order to extract these elements.

```python
# common24.py
import re
def extract_parameters(program):
    repeated_program = r"""inp w
mul x 0
add x z
mod x 26
div z (.*)
add x (.*)
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y (.*)
mul y x
add z y"""

    div_check_add = re.findall(repeated_program, program)
    assert (len(div_check_add) == 14), len(div_check_add)
    return [list(map(int, dca)) for dca in div_check_add]
```

Now, what is this 18 line program doing ? If we reverse-engineer the 18 instructions, we can rewrite it as a piece of python code:

```python
# based on
# https://www.reddit.com/r/adventofcode/comments/rnejv5/comment/hpuaphy/?utm_source=share&utm_medium=web2x&context=3
def subroutine(w, zdiv, xcheck, yadd):
    """w is our input"""
    x = z % 26  # store the last element of z in x
    z /= zdiv   # if zdiv == 26, pop the last element of z
    if x != w - xcheck:
        z = 26 * z + w + yadd   # push w + yadd to z
    return z
```

This subroutine is called repeatedly for all the inputs, with the various values of zdiv, xcheck and yadd. The resulting
z is then used as an input to the next subroutine.
Only the z register really changes: y is not used, and x is reset in each subroutine.

Given this knowledge, there are now many ways to solve this problem.


## Bottom-up approach

We can solve the problem by only knowing the subroutine: given the output, what are the inputs than can produce it?
We start from the end, where we know that z must be 0. We extract a list of the possible input that made z reach zero,
and the corresponding starting z.
Then we start over with the previous block, using our newly found list of z, and so on until the end.
For part 1, we pick the highest inputs, for part 2 we keep the lowest.

```python
from common24 import extract_parameters
import itertools as it

# https://gist.github.com/jkseppan/1e36172ad4f924a8f86a920e4b1dc1b1
def backward(xcheck, yadd, zdiv, z_final, w):
    """Returns the possible values of z before a single block
    if the final value of z is z_final and input is w
    """
    zs = []
    x = z_final - w - yadd
    if x % 26 == 0:
        zs.append(x // 26 * zdiv)
    if 0 <= w - xcheck < 26:
        z0 = z_final * zdiv
        zs.append(w - xcheck + z0)

    return zs


def solve(part, div_check_add):
    zs = {0}
    result = {}
    if part == 1:
        ws = list(range(1, 10))
    else:
        ws = list(range(9, 0, -1))
    for zdiv, xcheck, yadd in div_check_add[::-1]:
        newzs = set()
        for w, z in it.product(ws, zs):
            z0s = backward(xcheck, yadd, zdiv, z, w)
            for z0 in z0s:
                newzs.add(z0)
                result[z0] = (w,) + result.get(z, ())
        zs = newzs
    return ''.join(map(str, result[0]))

input = open("input/24_2021.txt").read()
div_check_add = extract_parameters(input)
print(solve(1, div_check_add))
print(solve(2, div_check_add))
```

Here is another solution that use this approach:
 - [explanation](https://www.reddit.com/r/adventofcode/comments/rnejv5/2021_day_24_solutions/hpu84cj/)
 - [code](https://topaz.github.io/paste/#XQAAAQCaBAAAAAAAAAA0m0pnuFI8c/fBNAn6x25rti77on4e8DYCelyI4Xj/SWO86l3MhYKSt/IwY1X8XDsPi6oUd359E/fP3WUCy+Hd0NBX3ScDH1UMDMoIn89DqtRJAkuU26H+bJQMhuQJZGvHfbRq+cNenkcVuZMyoJg2X38kr/tdzPWRs0R3nEQAYf3r0cXmSlac2aJH0P2sl7z4weDgKeKkKfE5swiQJ2MN12HwuoRR3LBTiJQjtT73JpWF+KtQBulka0/rhUSDOrztKM4biu1JoxqydIgyDfWupEKKtAiW75B1XW73P7TSQe8BI9O2T12ql8E/CBnsomkNwZLvIqQuyxA8lRBFyEb7T2Ofx8p8uaMPHbMv786Ho5P2KtCBwYdoX3z3fIV+cETYydTzjakKrUdUMq7dRV/kbM91elWwnwaxWByBhJS7jtOshbq8mO2W3BfCQ48WxEmwVrceIMSV2txALQlDxsy1lduebYKTzWCNl58cRdbnvICOxfoV9eofWAd6YP8WsL0eQUXcgzd8K1OW7qe67FH89TwqknLQ8KvTA3WKR1z4kubNHFXrvJLyFPO4Xqk5QhtviCMkBIiUic3Fvme1CyUV5V9g4XGkZpp95hCiTZFAtqVUvWvQARQNtGBuWv0mw9NB7qM940S7lQeCGHE95fH1UtwHYFdNrEuyPVdRYw6oCBD9+eh6PL+vkkN3dz3Axp2EUdlP/qwVQQ==)

## The top-down, stack/base 26 approach

Some people have visualized z as a base-26 number that behaves like a stack, where we push and pop values depending on some conditions.
 - [AoC 2021 day 24](https://github.com/kemmel-dev/AdventOfCode2021/blob/master/day24/AoC%20Day%2024.pdf)
 - See [def correct_input](https://topaz.github.io/paste/#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):

```python
[the subroutine] can be re-written using an if-block, which eliminates the x-register:

    if z % 26 + chk != inp:
        z //= div
        z *= 26
        z += inp + add
    else:
        z //= div

We note that "div" can only be one of two value: either 1 or 26. This
leads us to observe that all computations are manipulations of digits
of the z-register written in base 26. So it's natural to define
"div = 26**shf", so that "shf" will be either 0 or 1. We can use
binary operators to denote operations in base 26 as follows:

    z * 26  = z << 1
    z // 26 = z >> 1
    z % 26  = z & 1

With this we can write the program as follows:

    if z & 1 + chk != inp:
        z = z >> shf
        z = z << 1
        z = z + (inp + add)
    else:
        z = z >> shf

We can also write the bitwise operations as follows:

    z & 1 = z.last_bit
    z >> 1 = z.pop()
    (z << 1) & a = z.push(a)
    (z >> 1) << 1) & a = z.pop_push(a)

where pop/push refer to that bit stack of z in base 26 with the last
bit on top. Therefore, z.pop() removes the last bit, z.push(a) appends
the bit "a", and z.pop_push(a) replaces the last bit by "a".

Given that shf can only be 0 or 1 we get the following two cases:

    if shf == 0:
        if z.last_bit + chk != inp:
            z.push(inp + add)
    elif shf == 1:
        if z.last_bit + chk != inp:
            z.pop_push(inp + add)
        else:
            z.pop()

According to the puzzle input (our input) in all cases where shf == 0
it's true that chk > 9. Given that 1 <= inp <= 9 the check
(if z.last_bit + chk != inp) will therefore always be true. This gives:

    if shf == 0:
        z.push(inp + add)
    elif shf == 1:
        if z.last_bit + chk == inp:
            z.pop()
        else:
            z.pop_push(inp + add)

We can summarize in words. View z as a stack of bits in base 26. Start
with an empty stack. Whenever shf == 0 (div == 1) push (inp + add) on
the stack. If, however, shf == 1, consider the last bit on the stack.
If it's equal to (inp - chk), then remove it, otherwise replace it by
(inp + add).
```

(Let’s be clear: it took me a looot of time to get a good grasp of this approach, it’s OK if it doesn’t make sense right away).

We can then solve the problem very quickly, by searching for the correct input value in each 14 block. Occasionnaly, 
we’ll have to correct another value later on. It leads to a very fast solution:

```python
from common24 import extract_parameters
# https://topaz.github.io/paste/#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
def solve(inp, div_check_add) -> str:
    """Solve the problem by regarding z as a base 26 number"""
    zstack = []
    for i, oc in enumerate(div_check_add):
        zdiv, xcheck, yadd = oc
        if zdiv == 1:
            zstack.append((i, yadd))
        elif zdiv == 26:
            j, yadd = zstack.pop()
            inp[i] = inp[j] + yadd + xcheck
            if inp[i] > 9:
                inp[j] = inp[j] - (inp[i] - 9)
                inp[i] = 9
            if inp[i] < 1:
                inp[j] = inp[j] + (1 - inp[i])
                inp[i] = 1
        else:
            raise (ValueError(f"unsupported div value: {zdiv}"))
    assert (len(zstack) == 0), len(zstack) # the stack must be 0 in order for z to reach 0 at the end
    return "".join(map(str, inp))


def part1(div_check_add):
    "biggest accepted number"
    return solve(list([9] * 14), div_check_add)


def part2(div_check_add):
    """smallest accepted number"""
    return solve(list([1] * 14), div_check_add)


input = open("input/24_2021.txt").read()
div_check_add = extract_parameters(input)
print(part1(div_check_add))
print(part2(div_check_add))
```

## Using Z3

We can use Z3, a theorem solver, to solve the simplified subroutines for us. 

```python
from z3 import *
from common24 import extract_parameters


def solve(div_check_add: list, part: int) -> int:
    solver = Optimize()
    z = 0  # this is our running z, which has to be zero at the start and end
    # We have 14 inputs, they all are integers between 1 and 9 included
    ws = [Int(f'w{i}') for i in range(14)]
    for i in range(14):
        solver.add(And(ws[i] >= 1, ws[i] <= 9))
    # The value where we concatenate our input digits
    digits_base_10 = Int(f"digits_base_10")
    solver.add(digits_base_10 == sum((10 ** i) * d for i, d in enumerate(ws[::-1])))
    # We implement the subroutine as a list of constraints, one for each of the 14 blocks:
    for (i, [div, check, add]) in enumerate(div_check_add):
        z = If(z % 26 + check == ws[i], z / div, z / div * 26 + ws[i] + add)
    # The final z value must be zero
    solver.add(z == 0)
    if part == 1:
        solver.maximize(digits_base_10)
    else:
        solver.minimize(digits_base_10)
    assert (solver.check() == sat)  # the solver must find a solution
    return solver.model().eval(digits_base_10)


input = open("input/24_2021.txt").read()
div_check_add = extract_parameters(input)
print(solve(div_check_add, 1))
print(solve(div_check_add, 2))

```

## the hacker way: using GCC to simplify the equations, then using Z3

I’m keeping this here because that’s clever. [Mebeim had issues writing a 100% z3 solution](https://www.reddit.com/r/adventofcode/comments/rnejv5/comment/hps4c3n/?utm_source=share&utm_medium=web2x&context=3), so he used GCC to simplify the equations for him:

```python
 - Rewrite the [input program by hand in C](https://github.com/mebeim/aoc/blob/master/2021/misc/day24/program.c) (with a bunch of macros) and let GCC compile it with maximum optimizations.
 - Decompile the generated binary in IDA Pro (or [Ghidra](https://ghidra-sre.org/) if you want), which should give [a pretty good decompiled source with simplified equations](https://github.com/mebeim/aoc/blob/master/2021/misc/day24/decompiled.c ) (thanks GCC!).
 - Copy paste [the equations into a new Z3 Python script](https://github.com/mebeim/aoc/blob/master/2021/original_solutions/day24.py) and solve for the maximum/minimum using the Z3 Optimizer solver, which this time can manage to work in a decent runtime with the simplified equations (~30s).
```

# Generic solutions

In the second part, we are studying approach that could work for any ALU program, even if they did not have 
the properties we studied in the first part (repeated code, x and y are useless, and so on).

## Clever bruteforcing

The bruteforce way means going through all the possibilities. That O(n), but when n is large and the algorithm can be slow, 
it can take a lot of time. The problem itself involves going through **9^14 possibilities**. The naive bruteforce approach could mean at least a few days of computations.

Matt Keeter [wrote a detailled article](https://www.mattkeeter.com/blog/2021-12-27-brute/) about how he used **code generation, state deduplication and multithreading** in order to speed it up.

## Semi-generic: DFS + memoization

DFS in itself was to slow, so memoization helped avoid recomputing similar steps in other subroutines.
This is not totally generic since it takes advantage of the fact that the program consists in 14 repeated programs…
but that clever anyway.

```python
I noticed the input code had 14 very similar chunks that each took a single input, and the only thing that mattered about the state between chunks was z and input w registers -- x and y are zeroed out each time. So I basically just did a DFS with depth 14 and memoization on the branches, trying to find z=0 at the final step. And I added a cache for the execution to speed up part 2. Part 2 took 8 minutes runtime.
```

https://github.com/WilliamLP/AdventOfCode/blob/master/2021/day24.py

## Using Z3

The use of Z3 for this kind of reversing problem is quite popular in CTF contests.
I was surprised not to see it more often. With it, we can entirely bruteforce the problem
by simply describing the problem and adding constraints for the result of each instruction.

This is very similar to the previous z3 approach, except we implement all the instructions instead of the simplified routine.
Interestingly, both z3 solution run in about the same time.

```python
import z3
from common24 import parse_code
# https://www.reddit.com/r/adventofcode/comments/rnejv5/2021_day_24_solutions/hpshymr/
alu_program = parse_code(open('input/24_2021.txt', 'r').read())

solver = z3.Optimize()
# Two constants we’ll need later on
zero, one = z3.BitVecVal(0, 64), z3.BitVecVal(1, 64)
# our input digits
digits = [z3.BitVec(f'd_{i}', 64) for i in range(14)]
for d in digits:
    solver.add(z3.And(1 <= d, d <= 9))
digit_input = iter(digits)
# the base 10 result where we concatenate the values
digits_base_10 = z3.BitVec(f"digits_base_10", 64)
solver.add(digits_base_10 == sum((10 ** i) * d for i, d in enumerate(digits[::-1])))

# Now we implement the entire ALU program through Z3
registers = {r: zero for r in 'xyzw'}
for i, instruction in enumerate(alu_program):
    # for every instruction, we create an intermediate value whose constraint is to
    # hold the result of this instruction
    if instruction[0] == 'inp':
        registers[instruction[1]] = next(digit_input)
    else:
        register, operand = instruction[1:]
        operand = registers[operand] if operand in registers else int(operand)
        instruction_i = z3.BitVec(f'instruction_{i}', 64)
        if instruction[0] == 'add':
            solver.add(instruction_i == registers[register] + operand)
        elif instruction[0] == 'mul':
            solver.add(instruction_i == registers[register] * operand)
        elif instruction[0] == 'mod':
            solver.add(registers[register] >= 0)
            solver.add(operand > 0)
            solver.add(instruction_i == registers[register] % operand)
        elif instruction[0] == 'div':
            solver.add(operand != 0)
            solver.add(instruction_i == registers[register] / operand)
        elif instruction[0] == 'eql':
            solver.add(instruction_i == z3.If(registers[register] == operand, one, zero))
        else:
            assert False
        registers[register] = instruction_i

solver.add(registers['z'] == 0)

for f in (solver.maximize, solver.minimize):
    solver.push()
    f(digits_base_10)
    assert(solver.check() == z3.sat)
    print(solver.model().eval(digits_base_10))
    solver.pop()
```
  
## Using a custom symbolic calculation

Some warriors decided to implement an home made symbolic calculator, because why not?

 - [morgoth1145 wrote some explanation about his approach](https://www.reddit.com/r/adventofcode/comments/rnwz9p/2021_day_24_solving_the_alu_programmatically_with/)
 - [p88h shared his code too](https://github.com/p88h/aoc2021/blob/main/other/day24.py)
