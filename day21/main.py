import sys
import itertools

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

grid = {
    i + j*1j
    for i, line in enumerate(data.splitlines())
    for j, tile in enumerate(line)
    if tile in '.S'
}

N = max(int(p.real + 1) for p in grid)
mid = N//2
last = N - 1
S = mid + mid*1j

def walk(start, steps):
    ps = {start}
    for _ in range(steps):
        ps = {p + dp for p in ps for dp in (1, -1, 1j, -1j) if p + dp in grid}
    return len(ps)

p1 = walk(S, 64)
print(f"Part one: {p1}")

evens = walk(S, 2 * N)
odds = walk(S, 2 * N + 1)
corners = (0, last, last*1j, last + last*1j)
A = sum(walk(p, (3 * N - 3) // 2) for p in corners)
B = sum(walk(p, (N - 3) // 2) for p in corners)
midpoints = (mid, mid*1j, last + mid*1j, mid + last*1j)
T = sum(walk(p, N - 1) for p in midpoints)

Q = 26501365 // N
p2 = (Q - 1)**2*odds + Q**2*evens + (Q - 1)*A + Q*B + T

print(f"Part two: {p2}")
