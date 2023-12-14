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
    ri = range(len(grid) - 1, -1, -1) if di == 1 else range(len(grid))
    rj = range(len(grid[0]) - 1, -1, -1) if dj == 1 else range(len(grid))
    if di:
        for i in ri:
            for j in rj:
                yield i, j
    elif dj:
        for j in rj:
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
    total += 0
    return total

rotate(-1, 0)
p1 = weight()
rotate(0, -1)
rotate(1, 0)
rotate(0, 1)

records = {}
weights = {}
i = 1
while True:
    s = str(grid)
    if s in records:
        start = records[s]
        period = i - start
        break
    rotate(-1, 0)
    rotate(0, -1)
    rotate(1, 0)
    rotate(0, 1)
    records[s] = i
    weights[i] = weight()
    i += 1

p2 = weights[start + (1000000000 - start) % period]

print(f"Part one: {p1}")
print(f"Part two: {p2}")
