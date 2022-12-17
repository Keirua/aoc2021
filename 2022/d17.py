import pprint as pp

operations = open(f"d17.txt").read().strip()

flat_h = ["####"]
cross = [".#.","###",".#."]
reverse_l = ["..#", "..#", "###"]
flat_v = ["#", "#", "#", "#"]
square = ["##", "##"]
shapes = [flat_h, cross, reverse_l, flat_v, square]

class CurrentShape:
    def __init__(self):
        self.index = 0
        self.x = 3
        self.y = 3+1 # (bottom = 0)


# 0 = bottom of the board, so that we can happend new cells easily at the end
board = [list("#" * (7))] + [list(".......") for l in range(4)]
def debug(board):
    for l in board[::-1]:
        l2 = l.copy()
        print("".join(l2))

curr_shape = CurrentShape()

debug(board)