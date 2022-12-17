import pprint as pp

operations = open(f"d17.txt").read().strip()

flat_h = ["####"]
cross = [".#.", "###", ".#."]
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
        self.y = 3 + 1


# 0 = bottom of the board, so that we can happend new cells easily at the end
board = [list("#" * (7))] + [list(".......") for l in range(4)]


def draw(board, current_shape_info):
    curr_shape = shapes[curr_shape_info.index]
    for y in range(len(curr_shape)):
        for x in range(len(curr_shape[0])):
            bx, by = x + current_shape_info.x, y + current_shape_info.y
            print(y, by, len(board))
            if curr_shape[y][x] == "#" and board[by][bx] == ".":
                board[by][bx] = curr_shape[y][x]


def undraw(board, current_shape_info):
    curr_shape = shapes[curr_shape_info.index]
    for y in range(len(curr_shape)):
        for x in range(len(curr_shape[0])):
            if curr_shape[y][x] == "#":
                bx, by = x + current_shape_info.x, y + current_shape_info.y
                board[by][bx] = "."


def debug(board, current_shape_info, i):
    print(f"move {i}")
    draw(board, current_shape_info)
    for revy, l in enumerate(board[::-1]):
        l2 = l.copy()
        print("".join(l2))
    # print("\n")
    undraw(board, current_shape_info)


curr_shape_info = CurrentShape()


def can_move(board, curr_shape_info, xy):
    """Can the current shape move to coords xy?"""
    cx, cy = xy
    curr_shape = shapes[curr_shape_info.index]
    for y in range(len(curr_shape)):
        for x in range(len(curr_shape[0])):
            if x + cx >= 7 or y+cy >= len(board):
                return False
            val = board[y + cy][x + cx]
            if curr_shape[y][x] == "#" and val == "#":
                return False
    return True


def apply_jet(board, curr_shape_info, i):
    if operations[i % len(operations)] == "<":
        nx = curr_shape_info.x - 1
    else:
        nx = curr_shape_info.x + 1
    if 0 <= nx < 7 and can_move(board, curr_shape_info, (nx, curr_shape_info.y)):
        curr_shape_info.x = nx


def fall_down(board, curr_shape_info) -> bool:
    ny = curr_shape_info.y - 1
    if ny >= 0 and can_move(board, curr_shape_info, (curr_shape_info.x, ny)):
        curr_shape_info.y = ny
        return True
    return False

def find_highest_rock(board):
    for y in range(len(board)-1, 0, -1):
        for c in board[y]:
            if c == "#":
                return y

for i in range(10):
    if i % 2 == 0:
        apply_jet(board, curr_shape_info, i)
        debug(board, curr_shape_info, i)
    else:
        if not fall_down(board, curr_shape_info):
            debug(board, curr_shape_info, i)
            # Now we had the shape to the board
            draw(board, curr_shape_info)
            # Then we reset the shape info and move to the next shape
            curr_shape_info.index = (curr_shape_info.index + 1) % len(shapes)
            curr_shape_info.x = 2
            # We need to find the highest location, because we may need to increase the size of the drawing board
            max_y = find_highest_rock(board)
            curr_shape_info.y = max_y + 3
            if len(board) <= max_y + 4 + 2:
                while(len(board)) <= max_y + 4 + 2:
                    board.append(list("......."))
            curr_shape_info.y = max_y + 3
            # print(board)
