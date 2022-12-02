lines = open("d2.txt").readlines()
remap = {
    "A": "R",
    "B": "P",
    "C": "S",
    "X": "R",
    "Y": "P",
    "Z": "S"
}
moves =  [[remap[c] for c in l.strip().split(" ")] for l in lines]

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
shapes = {
    "R": 1,
    "P": 2,
    "S": 3,
}
scores_map = {
    1:6,
    0:3,
    -1:0
}
total = 0
for (opponent, you) in moves:
    print(opponent, you)
    score = compare(you, opponent)
    step = scores_map[score] + shapes[you]
    print(step)
    total += step
# print(moves)
print(total)