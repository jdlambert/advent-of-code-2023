import sys
import collections
import re

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

bricks = [tuple(int(v) for v in re.findall(r'\d+', line)) for line in data.splitlines()]
bricks.sort(key=lambda b: b[2])

tops = collections.defaultdict(lambda: (-1, -1))
above = collections.defaultdict(set)
below = collections.defaultdict(set)
for b, (i0, j0, k0, i1, j1, k1) in enumerate(bricks):
    max_top = 0
    for i in range(i0, i1 + 1):
        for j in range(j0, j1 + 1):
            top, support = tops[(i, j)]
            if top > max_top:
                max_top = top
                below[b].clear()
            if top == max_top:
                below[b].add(support)

    for support in below[b]:
        above[support].add(b)

    drop = k0 - max_top - 1
    for i in range(i0, i1 + 1):
        for j in range(j0, j1 + 1):
            tops[(i, j)] = (k1 - drop, b)

p1 = 0
p2 = 0

for b in range(len(bricks)):
    to_fall = [b]
    fallen = set()
    while to_fall:
        fall = to_fall.pop()
        if fall in fallen:
            continue
        fallen.add(fall)
        for supported in above[fall]:
            if not below[supported] - fallen:
                to_fall.append(supported)
    p1 += len(fallen) == 1
    p2 += len(fallen) - 1

print(f"Part one: {p1}")
print(f"Part two: {p2}")
