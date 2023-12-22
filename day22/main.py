import sys
import collections
import re

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

bricks = [tuple([int(v) for v in re.findall('\d+', line)]) for line in data.splitlines()]
bricks.sort(key=lambda b: b[2])

tops = collections.defaultdict(lambda: (0, -1))
above = collections.defaultdict(set)
below = collections.defaultdict(set)
for b, brick in enumerate(bricks):
    collision = max(
        tops[(i, j)][0]
        for i in range(brick[0], brick[3] + 1)
        for j in range(brick[1], brick[4] + 1)
    )

    below[b] = {
        tops[(i, j)][1]
        for i in range(brick[0], brick[3] + 1)
        for j in range(brick[1], brick[4] + 1)
        if tops[(i, j)][0] == collision
    }

    for b1 in below[b]:
        above[b1].add(b)

    dk = max(brick[2] - collision - 1, 0)
    for i in range(brick[0], brick[3] + 1):
        for j in range(brick[1], brick[4] + 1):
            tops[(i, j)] = (brick[5] - dk, b)

p1 = sum(1 for b in range(len(bricks)) if all(len(below[b1]) > 1 for b1 in above[b]))
p2 = 0

for b in range(len(bricks)):
    frontier = [b]
    fallen = set()
    while frontier:
        fall = frontier.pop()
        fallen.add(fall)
        for a in above[fall]:
            if not (below[a] - fallen):
                frontier.append(a)
    p2 += len(fallen) - 1

print(f"Part one: {p1}")
print(f"Part two: {p2}")
