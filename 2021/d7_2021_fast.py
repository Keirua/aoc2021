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