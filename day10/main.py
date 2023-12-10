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

frontier = [(si, sj)]
loop = set()

while frontier:
    i, j = frontier.pop()
    if (i, j) in loop:
        continue
    loop.add((i, j))
    for di, dj in pipes[grid[i][j]]:
        frontier.append((i + di, j + dj))

p1 = len(loop) // 2

frontier = [((si, sj), (0, 0))]
marked = {}

def neighbors(i0, j0):
    for i in range(i0 - 1, i0 + 2):
        for j in range(j0 - 1, j0 + 2):
            if in_bounds(i, j):
                yield (i, j)

def mark(i, j, sym):
    if not in_bounds(i, j):
        return
    frontier = [(i, j)]
    while frontier:
        i, j = frontier.pop()
        if (i, j) in loop or (i, j) in marked:
            continue
        marked[(i, j)] = sym
        for i1, j1 in neighbors(i, j):
            frontier.append((i1, j1))

mark_dir = {
    (-1, 0): (0, -1),
    (1, 0): (0, 1),
    (0, -1): (1, 0),
    (0, 1): (-1, 0),
}

seen = set()
while frontier:
    (i, j), d = frontier.pop()
    if (i, j) in seen:
        continue
    seen.add((i, j))
    for di, dj in pipes[grid[i][j]]:
        frontier.append(((i + di, j + dj), (di, dj)))
        mark_di, mark_dj = mark_dir[(di, dj)]
        mark(i + mark_di, j + mark_dj, 'X')
        mark(i + di + mark_di, j + dj + mark_dj, 'X')
        mark(i - mark_di, j - mark_dj, 'Y')
        mark(i + di - mark_di, j + dj - mark_dj, 'Y')

for i in range(len(grid)):
    if (i, 0) not in loop:
        ext_point = (i, 0)
        break

exterior = {m for m in marked if marked[m] == 'X'}
interior = {m for m in marked if marked[m] == 'Y'}
if marked[ext_point] == 'Y':
    exterior, interior = interior, exterior

print(f"Part one: {p1}")

mapping = {
    "F": "\u250F",
    "J": "\u251B",
    "L": "\u2517",
    "7": "\u2513",
    "|": "\u2503",
    "-": "\u2501",
}

mapping['S'] = mapping[s_pipe]

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
            
p2 = len(interior)

print(f"Part two: {p2}")
