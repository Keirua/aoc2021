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
        if self.is_in_grid(x, y):
            self.grid[y][x] = c

    def is_in_grid(self, x:int, y:int) -> bool:
        return 0 <= y < self.H and 0 <= x < self.W

    def get(self, x, y):
        if self.is_in_grid(x, y):
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

class SnowflakeAutomaton:
    def __init__(self, grid):
        self.g: Grid = grid
        self.curr_snowflake = Point(500, 0)
        self.nb_step = 0
        self.nb_sand = 0

    def run(self, part=1):
        while not self.drop_snowflake(part):
            pass

    def drop_snowflake(self, part=1):
        curr = Point(500, 0)
        self.nb_sand += 1
        while True:
            if part == 2 and self.g.get(500, 0) == "#":
                return True
            self.nb_step += 1
            ny = curr.y + 1
            if self.g.get(curr.x, ny) == "#" and self.g.get(curr.x-1, ny) == "#" and self.g.get(curr.x+1, ny) == "#":
                self.g.plot(curr.x, curr.y, "#")
                return False  # We managed to drop a snowflake
            if self.g.get(curr.x, ny) == "#" and self.g.get(curr.x-1, ny) == ".":
                curr.x -= 1
            if self.g.get(curr.x, ny) == "#" and self.g.get(curr.x-1, ny) == "#" and self.g.get(curr.x+1, ny) == ".":
                curr.x += 1
            curr.y = ny
            # are we done?
            if part == 1 and curr.y > self.g.max_y:
                return True

if __name__ == "__main__":
    lines = parse(d14)
    # lines = parse(d14_samples)
    # pp.pprint(lines)
    grid = Grid(lines)
    automaton = SnowflakeAutomaton(grid)
    automaton.run(part=1)
    # print(grid)
    print(automaton.nb_sand-1)

    # Part 2. Cheating a bit, it assumes there won’t be negative Xs
    lines.append(
        [(0, 2+grid.max_y), (1000, 2+grid.max_y)]
    )
    grid2 = Grid(lines)
    automaton2 = SnowflakeAutomaton(grid2)
    automaton2.run(part=2)
    # print(grid2)
    print(automaton2.nb_sand-1)

