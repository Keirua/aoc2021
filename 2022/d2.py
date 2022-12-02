lines="""A Y
B X
C Z""".split("\n")
lines = open("d2.txt").readlines()

remap = {
    "A": "R",
    "B": "P",
    "C": "S",
    "X": "R",
    "Y": "P",
    "Z": "S"
}
shapes = {
    "R": 1,
    "P": 2,
    "S": 3,
}
def part1(lines):
    moves = [[remap[c] for c in l.strip().split(" ")] for l in lines]

    def compare(a, b):
        if a == b:
            return 0
        if a == "R":
            if b == "P":
                return -1
            if b == "S":
                return 1
        if a == "P":
            if b == "R":
                return 1
            if b == "S":
                return -1
        if a == "S":
            if b == "R":
                return -1
            if b == "P":
                return 1

    scores_map = {
        1:6,
        0:3,
        -1:0
    }
    total = 0
    for (opponent, you) in moves:
        score = compare(you, opponent)
        step = scores_map[score] + shapes[you]
        total += step
    return total

def part2(lines):
    moves = [[c for c in l.strip().split(" ")] for l in lines]
    # x = lose, y = draw, z = win
    total = 0
    for (opponent, you) in moves:
        if you == "X": # lose
            rounds_res = 0
            if opponent == "A": # R
                move_res = shapes["S"]
            if opponent == "B": # P
                move_res = shapes["R"]
            if opponent == "C": # S
                move_res = shapes["P"]
        if you == "Y": # draw
            rounds_res = 3
            if opponent == "A": # R
                move_res = shapes["R"]
            if opponent == "B": # P
                move_res = shapes["P"]
            if opponent == "C": # S
                move_res = shapes["S"]
        if you == "Z": # win
            rounds_res = 6
            if opponent == "A": # R
                move_res = shapes["P"]
            if opponent == "B": # P
                move_res = shapes["S"]
            if opponent == "C": # S
                move_res = shapes["R"]
        print(opponent, you)
        print(move_res, rounds_res)
        step = move_res + rounds_res
        # print(step)
        print()

        total += step

    # print(moves)
    return total

total = part1(lines)
total2 = part2(lines)
# print(moves)
print(total2)