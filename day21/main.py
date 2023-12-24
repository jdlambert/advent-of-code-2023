import sys

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

grid = {
    i + j*1j
    for i, line in enumerate(data.splitlines())
    for j, tile in enumerate(line)
    if tile in '.S'
}

N = max(int(p.real + 1) for p in grid)

ps = [(N//2 + N//2*1j, 0)]
visited = {}
while ps:
    p, s = ps.pop()
    if p not in grid or p in visited:
        continue
    visited[p] = s
    ps.extend((p + dp, s + 1) for dp in (1, -1, 1j, -1j))

def constrain(pred):
    return sum(1 for v in visited.values() if pred(v))

print(f"Part one: {constrain(lambda v: v < 65 and v % 2 == 0)}")

EVEN = constrain(lambda v: v % 2 == 0)
ODD = constrain(lambda v: v % 2 != 0)
EVEN_CORNERS = constrain(lambda v: v % 2 == 0 and v > 65)
ODD_CORNERS = constrain(lambda v: v % 2 != 0 and v > 65)

Q = 26501365 // N
p2 = (Q + 1)**2*ODD + Q**2*EVEN - (Q + 1)*ODD_CORNERS + Q*EVEN_CORNERS

print(f"Part two: {p2}")
