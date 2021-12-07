import aoc
from collections import Counter

def parse(input):
    return Counter(aoc.all_ints(input))

def score(positions, align_at):
    return sum(abs(align_at - k) * positions[k] for k in positions.keys())

def cost2(n): return n * (n + 1) // 2

def score2(positions, align_at):
    return sum(positions[k] * cost2(abs(align_at - k)) for k in positions.keys())

def part1(positions):
    # all we have to do is minimize the score, and in order to do that the crabs have to go towards the center,
    # so they can move between the min and max values in the list.
    # We compute the cost of movement for each position over this range, and find the minimum
    return min(score(positions, i) for i in range(min(positions.keys()), max(positions.keys()) + 1))

def part2(positions):
    # same as part1, with a different scoring function
    return min(score2(positions, i) for i in range(min(positions.keys()), max(positions.keys()) + 1))

if __name__ == "__main__":
    input = aoc.input_as_string(aoc.challenge_filename(7, 2021))
    test_input = "16,1,2,0,4,2,7,1,2,14"

    positions = parse(input)
    test_positions = parse(test_input)

    assert (score(test_positions, 1) == 41)
    assert (score(test_positions, 3) == 39)
    assert (score(test_positions, 10) == 71)
    assert (part1(test_positions) == 37)
    print(part1(positions))
    assert (cost2(0) == 0)
    assert (cost2(1) == 1)
    assert (cost2(2) == 3)
    assert (cost2(5) == 15)
    assert (cost2(11) == 66)
    assert (score2(test_positions, 5) == 168)
    assert (score2(test_positions, 2) == 206)
    assert (part2(test_positions) == 168)
    assert (part2(positions) == 95167302)
    print(part2(positions))
