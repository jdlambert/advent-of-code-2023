import sys

with open(sys.argv[-1] if "x" in sys.argv else "input.txt") as f:
    data = f.read()

grid = data.splitlines()
for si, line in enumerate(grid):
    sj = line.find('S')
    if sj > -1:
        break

UP, DOWN, LEFT, RIGHT = ((-1, 0), (1, 0), (0, -1), (0, 1))

pipe_flow = {
    UP: {'|': UP, '7': LEFT, 'F': RIGHT},
    DOWN: {'|': DOWN, 'L': RIGHT, 'J': LEFT},
    LEFT: {'-': LEFT, 'L': UP, 'F': DOWN},
    RIGHT: {'-': RIGHT, '7': DOWN, 'J': UP},
}

s_dirs = []
for (di, dj) in [UP, DOWN, LEFT, RIGHT]:
    i, j = si + di, sj + dj
    if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
        if grid[i][j] in pipe_flow[(di, dj)]:
            s_dirs.append((di, dj))

i, j = si, sj
di, dj = s_dirs[0]
loop = set()
while (i, j) not in loop:
    loop.add((i, j))
    i, j = i + di, j + dj
    di, dj = pipe_flow[(di, dj)].get(grid[i][j], (0, 0))

interior = set()
for i, line in enumerate(grid):
    ext = True
    for j, tile in enumerate(line):
        if (i, j) in loop and (tile in "JL|" or tile == "S" and UP in s_dirs):
            ext = not ext
        elif (i, j) not in loop and not ext:
            interior.add((i, j))

if 'p' in sys.argv:
    for i, line in enumerate(grid):
        for j, tile in enumerate(line):
            if (i, j) in interior:
                print(f"\x1b[0;30;41m \x1b[0m", end='')
            elif (i, j) in loop:
                print(tile, end='')
            else:
                print(f"\x1b[0;30;47m \x1b[0m", end='')
        print("")
            
print(f"Part one: {len(loop) // 2}")
print(f"Part two: {len(interior)}")
