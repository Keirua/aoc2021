import aoc
from collections import Counter
from functools import partial

def parse(input): return aoc.all_ints(input)

def update_population_count(c):
    c2 = Counter()
    for i in range(1, 8+1):
        c2[i-1] = c[i]
    c2[6] += c[0]
    c2[8] += c[0]
    return c2

def count_population(ints, nb_steps=80):
    c = Counter(ints)
    for i in range(nb_steps):
        c = update_population_count(c)
    return sum(c.values())

if __name__ == "__main__":
    input = aoc.input_as_string(aoc.challenge_filename(6, 2021))
    test_input = "3,4,3,1,2"
    ints = parse(input)
    test_ints = parse(test_input)
    part1 = partial(count_population, nb_steps=80)
    part2 = partial(count_population, nb_steps=256)
    part3 = partial(count_population, nb_steps=10000)
    part4 = partial(count_population, nb_steps=150_000)
    part5 = partial(count_population, nb_steps=10**6) # about 5 seconds

    assert(count_population(test_ints, 18) == 26)
    assert(count_population(test_ints, 80) == 5934)
    assert(part2(test_ints) == 26984457539)

    print(part1(ints))
    print(part2(ints))
    print(part3(ints))
    print(part4(ints))
    # print(part5(ints))
    # print(part5(ints))
