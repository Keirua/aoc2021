import aoc
from statistics import median, mean

def parse(input): return list(map(int, input.split(",")))

def cost2(n): return n * (n + 1) // 2

def part1(positions):
    # The optimal position is on the median
    k = round(median(positions))
    return sum(abs(p-k) for p in positions)

def part2(positions):
    # The optimal position is close to the mean, and it can be proved that only 3 values are possible
    # https://www.reddit.com/r/adventofcode/comments/rawxad/2021_day_7_part_2_i_wrote_a_paper_on_todays/
    k = round(mean(positions))
    return min([sum(cost2(abs(k2-p)) for p in positions) for k2 in range(k-1, k+2)])

def nlogn_median(values):
    """"""
    values = sorted(values)
    l = len(values)
    # If the data set has an odd number of observations, the middle one is the median.
    if l %2 == 1:
        return values[l // 2]
    # If the data set has an even number of observations, there is no distinct middle value and
    # the median is usually defined to be the arithmetic mean of the two middle values
    return 0.5*(values[l // 2 - 1] + values[l // 2])

assert(nlogn_median([1, 3, 3, 6, 7, 8, 9]) == 6)
assert(nlogn_median([1, 2, 3, 4, 5, 6, 8, 9]) == (4+5)/2)

import random
def linear_median(values):
    # pick a random pivot
    pivot = random.choice(values)
    k = len(values) // 2
    # now we partition our list into two sub lists:
    #  - in lessers_or_equal_elts: all the values of the initial list that are <= the pivot
    #  - in greater_elts: all the values of the initial list that are > the pivot
    lessers_or_equal_elts = []
    greater_elts = []
    for v in values:
        if v <= pivot:
            lessers_or_equal_elts.append(v)
        else:
            greater_elts.append(v)
    # now, one of these groups contain the pivot

def quickselect():
    pass


if __name__ == "__main__":
    input = aoc.input_as_string(aoc.challenge_filename(7, 2021))
    test_input = "16,1,2,0,4,2,7,1,2,14"

    positions = parse(input)
    test_positions = parse(test_input)

    assert (part1(test_positions) == 37), part1(test_positions)
    print(part1(parse(input)))
    assert (part2(test_positions) == 168), part2(test_positions)
    assert (part2(positions) == 95167302)
    print(part2(positions))