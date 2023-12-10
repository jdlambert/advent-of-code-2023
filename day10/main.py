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

interior = set()

for i, line in enumerate(grid):
    inn = False
    for j, tile in enumerate(line):
        if tile == "S":
            tile = s_pipe
        if (i, j) in loop and tile in "JL|":
            inn = not inn
        if (i, j) not in loop and inn:
            interior.add((i, j))

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
            elif (i, j) in loop:
                print(mapping[tile], end='')
            else:
                print(f"\x1b[0;30;47m \x1b[0m", end='')
        print("")
            
print(f"Part one: {len(loop) // 2}")
print(f"Part two: {len(interior)}")
