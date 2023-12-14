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

records = [(0, weight(), str(grid))]
rotate(-1, 0)
p1 = weight()
rotate(0, -1)
rotate(1, 0)
rotate(0, 1)

def detect_cycle():
    for i0, w0, s0 in records[:-1]:
        i1, w1, s1 = records[-1]
        if w0 == w1 and s0 == s1:
            return i1 - i0
    return -1

i = 1
r = detect_cycle()
while r < 0:
    records.append((i, weight(), str(grid)))
    rotate(-1, 0)
    rotate(0, -1)
    rotate(1, 0)
    rotate(0, 1)
    r = detect_cycle()
    i += 1

a = records[-r - 1][0]

p2 = records[a + (1000000000 - a) % r][1]

print(f"Part one: {p1}")
print(f"Part two: {p2}")
