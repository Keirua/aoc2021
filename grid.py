COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[92m"
COLOR_NORMAL = "\033[0m"

class Grid:
    def __init__(self, w, h, value):
        self.w = w
        self.h = h
        self.lines = []
        for j in range(h):
            self.lines.append([value for _ in range(w)])

    def set(self, x, y, v):
        self.lines[y][x] = v

    def get(self, x, y):
        return self.lines[y][x]

    def all_coords(self):
        for x in range(self.w):
            for y in range(self.h):
                yield (x, y)

    def get_cell_color(self, v):
        return COLOR_NORMAL

    def __str__(self):
        """Display these values as a 2-D grid.
        Inspired by norvig’s sudoku: http://norvig.com/sudoku.html
        """
        width = 1 + max(len(self.lines[y]) for y in range(self.h))
        line = ""
        for l in self.lines:
            line += ''.join([self.get_cell_color(c)+str(c).center(width) for c in l]) + "\n"
        return line + COLOR_NORMAL

class SampleGrid(Grid):
    def __init__(self, lines):
        super().__init__(5,5,0)
        self.lines = lines

    def get_cell_color(self, v):
        return COLOR_GREEN if v is not None else COLOR_RED

if __name__ == "__main__":
    sample_values = [
        [22, 13, 17, 11,  0],
        [ 8,  2, 23,  4, 24],
        [21,  9, 14, 16,  7],
        [ 6, 10,  3, 18,  5],
        [ 1, 12, 20, 15, 19]
    ]

    g = SampleGrid(sample_values)
    g.set(4,2, None)
    print(g)