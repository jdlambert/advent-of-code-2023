import sys
import collections

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

grid = {
    i + j*1j
    for i, line in enumerate(data.splitlines())
    for j, tile in enumerate(line)
    if tile in '.S'
}

N = max(int(p.real + 1) for p in grid)

p1 = 0
ps = collections.deque([(N//2 + N//2*1j, 0)])
evens = set()
odds = set()
while ps:
    p, s = ps.popleft()
    if s == 65:
        p1 = len(evens)
    if s == (5 * N) // 2 + 1:
        break
    if p.real%N + p.imag%N*1j not in grid or p in evens or p in odds:
        continue
    if s & 1:
        odds.add(p)
    else:
        evens.add(p)
    ps.extend((p + dp, s + 1) for dp in (1, -1, 1j, -1j))

print(f"Part one: {p1}")

def constrain(s, i0, i1, j0, j1):
    return len([p for p in s if i0 <= p.real < i1 and j0 <= p.imag < j1])

EVEN = constrain(evens, 0, N, 0, N)
ODD = constrain(odds, 0, N, 0, N)
BIG_DIAG = sum(constrain(odds, *c) for c in [
    (N, 2*N, N, 2*N),
    (N, 2*N, -N, 0),
    (-N, 0, N, 2*N),
    (-N, 0, -N, 0)
])
LIL_DIAG = sum(constrain(odds, *c) for c in [
    (-2*N, -N, N, 2*N),
    (N, 2*N, 2*N, 3*N),
    (2*N, 3*N, -N, 0),
    (-N, 0, -2*N, -N)
])
TIP = sum(constrain(odds, *c) for c in [
    (-2*N, -N, 0, N),
    (0, N, 2*N, 3*N),
    (2*N, 3*N, 0, N),
    (0, N, -2*N, -N)
])

Q = 26501365 // N
p2 = (Q - 1)**2*ODD + Q**2*EVEN + (Q - 1)*BIG_DIAG + Q*LIL_DIAG + TIP

print(f"Part two: {p2}")
