import pprint
import statistics

import aoc

pp = pprint.PrettyPrinter(indent=4)

input = aoc.input_as_string(aoc.challenge_filename(10, 2021))
test_input = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

closing = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}
opening = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}
scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}
scores2 = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def parse(input):
    return aoc.as_lines(input)


def score1(line):
    stk = list()
    for c in line:
        if c in closing.keys():
            assert (len(stk) > 0)
            t = stk.pop()
            if t != closing[c]:
                return scores[c]
        else:
            stk.append(c)
    return 0


def score_from_stack(stk):
    total_score = 0
    while len(stk) > 0:
        letter = stk.pop()
        total_score = 5 * total_score + scores2[opening[letter]]
    return total_score


def score2(line):
    # Find the stack structure
    stk = list()
    for c in line:
        if c in closing.keys():
            assert (len(stk) > 0)
            t = stk.pop()
            assert (t == closing[c])
        else:
            stk.append(c)
    assert (len(stk) > 0)
    # Compute the score out of an incomplete structure
    return score_from_stack(stk)


def part1(lines:list) -> int:
    return sum([score1(line) for line in lines])


def part2(lines:list) -> int:
    valid_lines = list(filter(lambda x: score1(x) == 0, lines))
    return statistics.median([score2(line) for line in valid_lines])


if __name__ == "__main__":
    lines = parse(input)
    test_lines = parse(test_input)

    assert(part1(test_lines) == 26397)
    assert(part2(test_lines) == 288957)
    print(part1(lines))
    print(part2(lines))
