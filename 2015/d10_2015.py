import aoc
from functools import partial, reduce
from itertools import accumulate

def next_it(s):
    s2 = ""
    prev = s[0]
    counter = 1
    for i in range(1, len(s)):
        if s[i] == prev:
            counter += 1
        else:
            s2 += f"{counter}{prev}"
            prev = s[i]
            counter = 1
    s2 += f"{counter}{prev}"
    return s2

assert(next_it("1") == "11")
assert(next_it("11") == "21")
assert(next_it("21") == "1211")
assert(next_it("1211") == "111221")
assert(next_it("111221") == "312211")

# def look_and_say(input, nb_iterations=40):
#     n = input
#     for i in range(nb_iterations):
#         n = next_it(n)
#     return len(n)
# It can be done with itertools too:
# def look_and_say(input, nb_iterations=40):
#     l = lambda a, b: next_it(a)
#     iterations = accumulate(range(nb_iterations), l, initial=input)
#     return len(list(iterations)[-1])
def look_and_say(input, nb_iterations=40):
    # we need to introduce a lambda
    l = lambda a, b: next_it(a)
    final_value = reduce(l, range(nb_iterations), input)
    return len(final_value)

part1 = partial(look_and_say, nb_iterations=40)
part2 = partial(look_and_say, nb_iterations=50)

input = aoc.input_as_string(aoc.challenge_filename(10, 2015))

print(part1(input))
print(part2(input))