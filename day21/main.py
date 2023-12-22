import sys
import itertools

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

grid = {
    i + j*1j: tile
    for i, line in enumerate(data.splitlines())
    for j, tile in enumerate(line)
    if tile in '.S'
}

N = max(int(p.real + 1) for p in grid)

frontier = {p for p in grid if grid[p] == 'S'}

p1 = 0
p2 = 0
target = 26501365

vals = []

for i in itertools.count(1):
    frontier = {
          p + dp for p in frontier for dp in (1, -1, 1j, -1j)
          if (p + dp).real % N + (p + dp).imag % N * 1j in grid
    }
    if i == 64:
        p1 = len(frontier)
    if i % N == target % N:
        vals.append(len(frontier))
        if len(vals) == 3:
            break

q = target // N
a, b, c = [b - a for a, b in zip([0] + vals, vals)]
p2 = a + q*b + q*(q - 1)*(c - b)//2

print(f"Part one: {p1}")
print(f"Part two: {p2}")
