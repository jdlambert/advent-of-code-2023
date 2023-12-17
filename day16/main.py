import sys

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

grid = data.splitlines()

N, E, S, W = (-1, 0), (0, 1), (1, 0), (0, -1)

def reflect(i, j, dir):
    tile = grid[i][j]
    if tile == '.' or tile == '|' and dir in (N, S) or tile == '-' and dir in (E, W):
        return [(i + dir[0], j + dir[1], dir)]
    if tile == '|':
        return [(i + dir[0], j + dir[1], dir) for dir in (N, S)]
    if tile == '-':
        return [(i + dir[0], j + dir[1], dir) for dir in (E, W)]
    if tile == '\\':
        dir = {E: S, S: E, N: W, W: N}[dir]
        return [(i + dir[0], j + dir[1], dir)]
    dir = {E: N, N: E, S: W, W: S}[dir]
    return [(i + dir[0], j + dir[1], dir)]

def in_bounds(i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

def energize(start):
    frontier = [start]
    visited = set()
    dir_visited = set()

    while frontier:
        cur = frontier.pop()
        if not in_bounds(*cur[:2]) or cur in dir_visited:
            continue
        dir_visited.add(cur)
        visited.add(cur[:2])
        frontier.extend(reflect(*cur))

    return len(visited)

p1 = energize((0, 0, E))

entries = (
    [(i, 0, E) for i in range(len(grid))] +
    [(i, len(grid[0]) - 1, W) for i in range(len(grid))] +
    [(0, j, S) for j in range(len(grid[0]))] +
    [(len(grid) - 1, j, N) for j in range(len(grid[0]))]
)

p2 = max(energize(entry) for entry in entries)

print(f"Part one: {p1}")
print(f"Part two: {p2}")
