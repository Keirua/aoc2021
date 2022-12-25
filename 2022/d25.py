import aoc
import re, pprint, itertools as it

pp = pprint.PrettyPrinter(indent=4)

input = open(f"d25.txt").read()
# input = open(f"d25-sample.txt").read()
lines = input.split("\n")


def sctoi(c):
    try:
        return int(c)
    except:
        if c == "-":
            return -1
        if c == "=":
            return -2


def snafu_to_i(s):
    out = 0
    coef = 1
    for c in s[::-1]:
        out += sctoi(c) * coef
        coef *= 5
    return out


def i_to_snafu(i: int):
    out = []
    coef = 1
    while coef < i:
        coef *= 5
    coef //= 5
    # First pass where we extract the coefs
    while coef > 0:
        val = i // coef
        i %= coef
        coef //= 5
        out.append(val)
    # Then we remap in the [-2, -1, 0, 1, 2] space with the transforms
    # described in the examples
    pos = len(out) -1
    while(pos) > 0:
        if out[pos] == 3:
            out[pos-1] += 1
            out[pos] = -2
        if out[pos] == 4:
            out[pos - 1] += 1
            out[pos] = -1
        if out[pos] == 5:
            out[pos-1] += 1
            out[pos] = 0
        pos -= 1

    # Then we convert to str
    mapping = {
        -1: "-",
        -2: "=",
        0: "0", 1: "1", 2: "2"
    }
    return "".join([mapping[o] for o in out])

def part1(lines):
    s = sum(map(snafu_to_i, lines))
    print(i_to_snafu(s))

assert (i_to_snafu(10) == "20")
assert (i_to_snafu(201) == "2=01")
assert (i_to_snafu(4890) == "2=-1=0")
part1(lines)
