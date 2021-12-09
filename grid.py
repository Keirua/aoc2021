COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[92m"
COLOR_NORMAL = "\033[0m"


class Grid:
    def __init__(self, w=0, h=0, lines=[]):
        self.w = w
        self.h = h
        self.lines = lines

    @classmethod
    def from_value(cls, w, h, value=0):
        return cls(w, h, [[value for _ in range(w)] for _ in range(h)])

    @classmethod
    def from_lines(cls, lines):
        return cls(len(lines[0]), len(lines), lines)

    def __setitem__(self, p, value):
        self.lines[p[1]][p[0]] = value

    def __getitem__(self, p):
        return self.lines[p[1]][p[0]]

    def set(self, x, y, v):
        self.lines[y][x] = v

    def get(self, x, y):
        return self.lines[y][x]

    def is_in_grid(self, p) -> bool:
        return 0 <= p[0] < self.w and 0 <= p[1] < self.h

    def neighbours4(self, p):
        offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        x, y = p
        return [(x + dx, y + dy) for (dx, dy) in offsets if self.is_in_grid((x + dx, y + dy))]

    def all_coords(self):
        for x in range(self.w):
            for y in range(self.h):
                yield x, y

    def get_cell_color(self, v):
        return COLOR_NORMAL

    def floodfill(self, start, cond_is_matched):
        """Find the neighbouring points using flood filling"""
        from collections import deque
        matching_points = [start]
        visited = [start]
        queue = deque(self.neighbours4(start))
        while len(queue) > 0:
            t = queue.popleft()
            if t not in visited and cond_is_matched(self[t]):
                matching_points.append(t)
                visited.append(t)

                for n in self.neighbours4(t):
                    queue.append(n)

        return matching_points

    def __str__(self):
        """Display these values as a 2-D grid.
        Inspired by norvig’s sudoku: http://norvig.com/sudoku.html
        """
        width = 1 + max([len(str(self.lines[y][x])) for (x, y) in self.all_coords()])
        text = ""
        for line in self.lines:
            text += ''.join([self.get_cell_color(c) + str(c).center(width) for c in line]) + "\n"
        return text + COLOR_NORMAL


if __name__ == "__main__":
    class SampleGrid(Grid):
        """A grid to demo color implementation"""

        def get_cell_color(self, v):
            return COLOR_GREEN if v is not None else COLOR_RED


    sample_values = [
        [22, 13, 17, 11, 0],
        [8, 2, 22, 4, 24],
        [21, 9, 14, 16, 7],
        [6, 10, 3, 17, 5],
        [1, 12, 20, 15, 19]
    ]

    g = SampleGrid.from_lines(sample_values)

    print(g)
    points = g.floodfill((1, 1), lambda v: v % 2 == 0)
    for p in points:
        g[p] = None
    g.set(4, 4, None)
    print(g)
    print()
    g2 = SampleGrid.from_value(5, 5, 42)
    print(g2)
