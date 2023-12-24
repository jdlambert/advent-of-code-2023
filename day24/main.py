import sys
import re

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

stones = [tuple(int(d) for d in re.findall(r'-?\d+', line)) for line in data.splitlines()]

lo, hi = (7, 27) if "x" in sys.argv else (200000000000000, 400000000000000)

PARALLEL = float("inf")
def IJ(s):
    return (s[0], s[1], s[3], s[4])
def IK(s):
    return (s[0], s[2], s[3], s[5])

p1 = 0

def collide(s0, s1, getter, dr=(0, 0)):
    i0, j0, di0, dj0 = getter(s0)
    i1, j1, di1, dj1 = getter(s1)
    di0 -= dr[0]
    di1 -= dr[0]
    dj0 -= dr[1]
    dj1 -= dr[1]
    det = di1*dj0 - dj1*di0
    if det == 0:
        return PARALLEL
    di = i1 - i0
    dj = j1 - j0
    t0 = (dj*di1 - di*dj1) / det
    t1 = (dj*di0 - di*dj0) / det
    if t0 <= 0 or t1 <= 0:
        return None
    return (i0 + t0*di0, j0 + t0*dj0)

for i, s0 in enumerate(stones):
    for s1 in stones[i + 1:]:
        collision = collide(s0, s1, IJ)
        p1 += collision is not None and collision is not PARALLEL and all(lo <= p <= hi for p in collision)

print(f"Part one: {p1}")

def collisions(di, dj, getter):
    ij = None
    for i, s0 in enumerate(stones):
        for s1 in stones[i + 1:]:
            collision = collide(s0, s1, getter, (di, dj))
            if collision is PARALLEL:
                continue
            if collision is None:
                return None
            if ij is not None and collision != ij:
                return None
            ij = collision
    return ij

for di in range(-256, 256):
    for dj in range(-256, 256):
        ij = collisions(di, dj, IJ)
        if ij is not None:
            for dk in range(-256, 256):
                ik = collisions(di, dk, IK)
                if ik is not None:
                    print(f"Part two: {int(ij[0] + ij[1] + ik[1])}")
                    break
            break
