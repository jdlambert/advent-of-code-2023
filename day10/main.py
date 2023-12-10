import sys

with open(sys.argv[-1] if "x" in sys.argv else "input.txt") as f:
    data = f.read()

grid = data.splitlines()
for si, line in enumerate(grid):
    sj = line.find('S')
    if sj > -1:
        break

pipes = {
    '|': ((-1, 0), (1, 0)),
    '-': ((0, -1), (0, 1)),
    'L': ((-1, 0), (0, 1)),
    'J': ((-1, 0), (0, -1)),
    '7': ((0, -1), (1, 0)),
    'F': ((0, 1), (1, 0)),
}

def in_bounds(i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

def neighbors(i0, j0):
    for i in range(i0 - 1, i0 + 2):
        for j in range(j0 - 1, j0 + 2):
            yield (i, j)

# Determine what type of pipe S is acting as

adj_pipes = []
for (di, dj) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
    i, j = si + di, sj + dj
    if in_bounds(i, j):
        pipe = grid[i][j]
        if pipe not in pipes:
            continue
        for ddi, ddj in pipes[pipe]:
            if (i + ddi, j + ddj) == (si, sj):
                adj_pipes.append((di, dj))
assert len(adj_pipes) == 2
for pipe, deltas in pipes.items():
    if sorted(deltas) == sorted(adj_pipes):
         s_pipe = pipe
         break

pipes['S'] = pipes[s_pipe]

# Discover the loop via DFS

frontier = [(si, sj)]
loop = set()
while frontier:
    i, j = frontier.pop()
    if (i, j) in loop:
        continue
    loop.add((i, j))
    for di, dj in pipes[grid[i][j]]:
        frontier.append((i + di, j + dj))

marked = {}
edge_mark = None
def mark(i0, j0, sym):
    global edge_mark
    frontier = [(i0, j0)]
    while frontier:
        i, j = frontier.pop()
        if (i, j) in loop or (i, j) in marked:
            continue
        if in_bounds(i, j):
            marked[(i, j)] = sym
            for i1, j1 in neighbors(i, j):
                frontier.append((i1, j1))
        else:
            edge_mark = sym

x_dir = {
    (-1, 0): (0, -1),
    (1, 0): (0, 1),
    (0, -1): (1, 0),
    (0, 1): (-1, 0),
}

# Mark the non-loop region to the left of the direction of travel X, to the right Y
# If we travel clockwise, X will be exterior and Y interior
# Vice-versa for counterclockwise
# We mark the grid edge in the same way for an easy way to identify the exterior

seen = set()
frontier = [(si, sj, (0, 0))]
while frontier:
    i, j, d = frontier.pop()
    if (i, j) in seen:
        continue
    seen.add((i, j))
    if grid[i][j] != 'S':
        xdi, xdj = x_dir[d]
        di, dj = d
        mark(i + xdi, j + xdj, 'X')
        mark(i - di + xdi, j - dj + xdj, 'X')
        mark(i - xdi, j - xdj, 'Y')
        mark(i - di - xdi, j - dj - xdj, 'Y')
    for di, dj in pipes[grid[i][j]]:
        frontier.append(((i + di, j + dj, (di, dj))))
        
exterior = {m for m in marked if marked[m] == 'X'}
interior = {m for m in marked if marked[m] == 'Y'}
if edge_mark == 'Y':
    exterior, interior = interior, exterior

mapping = {
    "F": "\u250F",
    "J": "\u251B",
    "L": "\u2517",
    "7": "\u2513",
    "|": "\u2503",
    "-": "\u2501",
}

mapping['S'] = mapping[s_pipe]

# Optionally, print a visual aid

if 'p' in sys.argv:
    for i, line in enumerate(grid):
        for j, tile in enumerate(line):
            if (i, j) in interior:
                print(f"\x1b[0;30;41m \x1b[0m", end='')
            elif (i, j) in exterior:
                print(f"\x1b[0;30;47m \x1b[0m", end='')
            elif (i, j) in loop:
                print(mapping[tile], end='')
            else:
                print(f"\x1b[0;30;42m \x1b[0m", end='')
        print("")
            
print(f"Part one: {len(loop) // 2}")
print(f"Part two: {len(interior)}")
