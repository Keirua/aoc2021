import re
import string
import os
import sys
# d1.py has input file d1.txt if no param is provided, else the last param is used as input file
input_file = sys.argv[-1] if len(sys.argv) > 1 else os.path.basename(__file__).replace(".py", ".txt")

def is_valid(dct):
    return dct.get("red", 0) <= 12 and dct.get("green", 0) <= 13 and dct.get("blue", 0) <= 14

with open(input_file) as f:
    lines = f.readlines()
    p1 = 0
    for line in lines:
        game, sets = line.rstrip().split(": ")
        game_id = int(game.split(" ")[-1])
        # print(game_id)
        # print(game, sets)
        subsets = sets.split(";")
        ok = True
        for subset in subsets:
            dices = re.findall(r"(\d+) (red|blue|green)", subset)
            dct = {d: int(nb) for nb, d in dices}
            if not is_valid(dct):
                ok = False
                break
        if ok:
          p1 += game_id
        # print(subsets)
    print(p1)
# print(lines)
