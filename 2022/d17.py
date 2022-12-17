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
        # Each rock appears so that its left edge is two units away from the left wall and
        # its bottom edge is three units above the highest rock in the room (or the floor, if there isn't one).
        self.x = 2
        self.y = 3+1


# 0 = bottom of the board, so that we can happend new cells easily at the end
board = [list("#" * (7))] + [list(".......") for l in range(4)]

def draw(board, current_shape_info):
    curr_shape = shapes[curr_shape_info.index]
    for y in range(len(curr_shape)):
        for x in range(len(curr_shape[0])):
            val = board[y+current_shape_info.y][x+current_shape_info.x]
            if curr_shape[y][x] == "#" and val == ".":
                board[y+current_shape_info.y][x+current_shape_info.x] = curr_shape[y][x]

def undraw(board, current_shape_info):
    curr_shape = shapes[curr_shape_info.index]
    for y in range(len(curr_shape)):
        for x in range(len(curr_shape[0])):
            if curr_shape[y][x] == "#":
                board[y+current_shape_info.y][x+current_shape_info.x] = "."

def debug(board, current_shape_info):
    draw(board, current_shape_info)
    for revy, l in enumerate(board[::-1]):
        l2 = l.copy()
        print("".join(l2))
    undraw(board, current_shape_info)


curr_shape_info = CurrentShape()

for i in range(4):
    print(f"move {i}")
    debug(board, curr_shape_info)