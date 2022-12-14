import re, pprint, itertools as it

pp = pprint.PrettyPrinter(indent=4)

d14 = open(f"d14.txt").read()
d14_samples = open(f"d14-sample.txt").read()


def parse(text: str):
    input_lines = text.strip().split("\n")
    lines = []
    for l in input_lines:
        lines.append([(int(x), int(y)) for (x, y) in re.findall(r"(\d+),(\d+)", l)])
    return lines


class Grid:
    def __init__(self, lines):
        # Extract the grid dimensions
        Xs = [x for l in lines for (x, y) in l]
        Ys = [y for l in lines for (x, y) in l]
        self.min_x = min(Xs)
        self.min_y = min(Ys)
        self.max_y = max(Ys)
        self.max_x = max(Xs)
        # self.W = max(Xs) - min(Xs)
        # self.H = max(Ys) - min(Ys)
        self.W = max(Xs) +1
        self.H = max(Ys) +1
        # Setup the empty grid
        self.grid = [["." for _ in range(self.W)] for _ in range(self.H)]
        # Plot all the rocks
        for l in lines:
            for i in range(len(l) - 1):
                x1, y1 = l[i]
                x2, y2 = l[i + 1]
                # Vertical line
                if x1 == x2:
                    for j in range(min(y1, y2), max(y1, y2) + 1):
                        self.plot(x1, j, "#")
                # Horizontal line
                if y1 == y2:
                    for j in range(min(x1, x2), max(x1, x2) + 1):
                        self.plot(j, y1, "#")


    def plot(self, x, y, c):
        if 0 <= y < self.H and 0 <= x < self.W:
        # self.grid[y - self.min_y][x - self.min_x] = c
            self.grid[y][x] = c

    def get(self, x, y):
        if 0 <= y < self.H and 0 <= x < self.W:
        # return self.grid[y - self.min_y][x - self.min_x]
            return self.grid[y][x]
        return "."

    def __repr__(self):
        # Display the grid
        out = ""
        for l in self.grid:
            out += "".join(l) + "\n"
        return out
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
START_SNOWFLAKE = (500, 500)
class Automaton:
    def __init__(self, grid):
        self.g:Grid = grid
        self.curr_snowflake = Point(500, 0)
        self.nb_step = 0
        self.nb_sand = 0
    def run(self):
        for i in range(100000):
            if self.drop_snowflake():
                break

    def drop_snowflake(self):
        curr = Point(500, 0)
        self.nb_sand += 1
        while True:
            self.nb_step += 1
            ny = curr.y + 1
            print(curr.x, curr.y)
            # The next 3 pixels
            if self.g.get(curr.x, ny) == "#" and self.g.get(curr.x-1, ny) == "#" and self.g.get(curr.x+1, ny) == "#":
                self.g.plot(curr.x, curr.y, "#")
                return False  # We managed to drop a snowflake
            if self.g.get(curr.x, ny) == "#" and self.g.get(curr.x-1, ny) == ".":
                curr.x -= 1
            if self.g.get(curr.x, ny) == "#" and self.g.get(curr.x-1, ny) == "#" and self.g.get(curr.x+1, ny) == ".":
                curr.x += 1
            curr.y = ny
            if curr.y > self.g.max_y:
                print("done")
                return True

            # # The pixel below is a snowflake
            # if self.g.get(curr.x, ny) == "#":
            #     # If there is no snowflake on the diagonal left, we had it
            #     if self.g.get(curr.x-1, ny) != "#":
            #         self.g.plot(curr.x-1, ny, "#")
            #         return False  # We managed to drop a snowflake
            #     # If there is a snowflake on the diagonal left, but not on the right, we had it
            #     if self.g.get(curr.x-1, ny) == "#" and self.g.get(curr.x+1, ny) != "#":
            #         self.g.plot(curr.x+1, ny, "#")
            #         return False  # We managed to drop a snowflake
            #     # There already are snowflakes on left and right
            #     if self.g.get(curr.x - 1, ny) == "#" and self.g.get(curr.x + 1, ny) == "#":
            #         # If we didn’t plot curr already:
            #         if self.g.get(curr.x, curr.y) != "#":
            #             self.g.plot(curr.x, curr.y, "#")
            #             return False  # We managed to drop a snowflake
            #         else:
            #             if self.g.get(curr.x - 1, curr.y) != "#":
            #                 curr.x -= 1
            #             elif self.g.get(curr.x + 1, curr.y) != "#":
            #                 curr.x += 1
            #             else:
            #                 return False



lines = parse(d14)
# lines = parse(d14_samples)
pp.pprint(lines)

grid = Grid(lines)
automaton = Automaton(grid)
automaton.run()
print(grid)
print(automaton.nb_sand-1)
# grid.plot(500,0,"T")
# print(grid)
