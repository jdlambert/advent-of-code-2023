import re
import collections

with open("input.txt") as f:
    data = f.read()

grid = data.splitlines()

symbols = set()

def neighbors(i0, j0, j1):
    for i in range(i0 - 1, i0 + 2):
        for j in range(j0 - 1, j1 + 1):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                yield grid[i][j]

p1 = 0

nums = collections.defaultdict(dict)

def num_neighbors(i0, j0):
    for i in range(i0 - 1, i0 + 2):
        for j in range(j0 - 1, j0 + 2):
            if i in nums and j in nums[i]:
                yield nums[i][j]


for i, line in enumerate(grid):
    matches = re.finditer(r'\d+', line)
    for match in matches:
        if any(n not in '0123456789.' for n in neighbors(i, match.start(), match.end())):
            p1 += int(match.group(0), 10)
        for j in range(match.start(), match.end()):
            nums[i][j] = match

p2 = 0

for i, line in enumerate(grid):
    for j, char in enumerate(line):
        if char not in '0123456789.':
            adjacent = list({n for n in num_neighbors(i, j)})
            if len(adjacent) == 2:
                p2 += int(adjacent[0].group(0), 10) * int(adjacent[1].group(0), 10)

print(f"Part one: {p1}")
print(f"Part two: {p2}")
