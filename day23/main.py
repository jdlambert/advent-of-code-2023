import sys
import collections

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

lines = data.splitlines()
grid = {i + j*1j: c for i, line in enumerate(lines) for j, c in enumerate(line) if c != '#'}
start = data.index('.')*1j
target = len(lines) - 1 + lines[-1].index('.')*1j

frontier = [(start, 0, set())]
p1 = float("-inf")
while frontier:
    p, s, seen = frontier.pop()
    if p in seen or p not in grid:
        continue
    if p == target:
        p1 = max(p1, s)
    else:
        match grid[p]:
            case '.':
                frontier.extend((p + dp, s + 1, seen | {p}) for dp in (1, 1j, -1, -1j))
            case 'v':
                frontier.append((p + 1, s + 1, seen | {p})) 
            case '>':
                frontier.append((p + 1j, s + 1, seen | {p}))

def outgoing(p):
    return sum(1 for dp in (1, 1j, -1, -1j) if p + dp in grid)

nodes = {start, target} | {p for p in grid if outgoing(p) > 2}
edges = collections.defaultdict(dict)
for node in nodes:
    frontier = [(node, 0)]
    seen = set()
    while frontier:
        p, s = frontier.pop()
        if p in seen or p not in grid:
            continue
        seen.add(p)
        if p != node and p in nodes:
            edges[node][p] = s
        else:
            frontier.extend((p + dp, s + 1) for dp in (1, 1j, -1, -1j))

frontier = [(start, 0, set())]
p2 = float("-inf")
while frontier:
    p, s, seen = frontier.pop()
    if p in seen:
        continue
    seen.add(p)
    if p == target:
        p2 = max(p2, s)
    else:
        frontier.extend((np, s + edges[p][np], seen | {p}) for np in edges[p])

print(f"Part one: {p1}")
print(f"Part two: {p2}")
