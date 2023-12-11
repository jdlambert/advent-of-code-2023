import sys
import math

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

grid = data.splitlines()

empty_rows = []
for i, row in enumerate(grid):
    if '#' not in row:
        empty_rows.append(i)

empty_cols = []
for j in range(len(grid[0])):
    if all(grid[i][j] != '#' for i in range(len(grid))):
        empty_cols.append(j)

stars = []
for i, line in enumerate(grid):
    for j, tile in enumerate(line):
        if tile == '#':
            stars.append((i, j))

def between(l, a, b):
    return sum(1 for x in l if a < x < b or b < x < a)

p1 = 0
p2 = 0
for i, (i0, j0) in enumerate(stars):
    for i1, j1 in stars[i + 1:]:
        p1 += abs(i1 - i0) + between(empty_rows, i0, i1)
        p1 += abs(j1 - j0) + between(empty_cols, j0, j1)
        p2 += abs(i1 - i0) + 999999 * between(empty_rows, i0, i1)
        p2 += abs(j1 - j0) + 999999 * between(empty_cols, j0, j1)
        
print(f"Part one: {p1}")
print(f"Part two: {p2}")
