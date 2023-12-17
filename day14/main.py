import sys

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

grid = [list(line) for line in data.splitlines()]

def find(i, j, di, dj):
    while 0 <= i + di < len(grid) and 0 <= j + dj < len(grid):
        if grid[i + di][j + dj] in '#O':
            return i, j
        i += di
        j += dj
    return i, j

def enum(di, dj):
    ri, rj = range(len(grid)), range(len(grid[0]))
    if di:
        for i in reversed(ri) if di == 1 else ri:
            for j in rj:
                yield i, j
    else:
        for j in reversed(rj) if dj == 1 else rj:
            for i in ri:
                yield i, j

def rotate(di, dj):
    for i, j in enum(di, dj):
        if grid[i][j] == 'O':
            new_i, new_j = find(i, j, di, dj)
            grid[i][j] = '.'
            grid[new_i][new_j] = 'O'

def weight():
    total = 0
    for i, line in enumerate(grid):
        for tile in line:
            if tile == 'O':
                total += len(grid) - i
    return total

rotate(-1, 0)
p1 = weight()
rotate(0, -1)
rotate(1, 0)
rotate(0, 1)

records = {}
weights = {}
i = 1
s = str(grid)
while s not in records:
    records[s] = i
    weights[i] = weight()
    rotate(-1, 0)
    rotate(0, -1)
    rotate(1, 0)
    rotate(0, 1)
    i += 1
    s = str(grid)

start = records[s]
period = i - start
p2 = weights[start + (1000000000 - start) % period]

print(f"Part one: {p1}")
print(f"Part two: {p2}")
