import sys
import re

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

stones = [tuple(int(d) for d in re.findall(r'-?\d+', line)) for line in data.splitlines()]

lo, hi = (7, 27) if "x" in sys.argv else (200000000000000, 400000000000000)

PARALLEL = float("inf")

p1 = 0

def collide_ij(s0, s1, dr=(0, 0)):
    i0, j0, _, di0, dj0, _ = s0
    i1, j1, _, di1, dj1, _ = s1
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

def collide_ik(s0, s1, dr=(0, 0)):
    i0, _, k0, di0, _, dk0 = s0
    i1, _, k1, di1, _, dk1 = s1
    di0 -= dr[0]
    di1 -= dr[0]
    dk0 -= dr[1]
    dk1 -= dr[1]
    det = di1*dk0 - dk1*di0
    if det == 0:
        return PARALLEL
    di = i1 - i0
    dk = k1 - k0
    t0 = (dk*di1 - di*dk1) / det
    t1 = (dk*di0 - di*dk0) / det
    if t0 <= 0 or t1 <= 0:
        return None
    return (i0 + t0*di0, k0 + t0*dk0)

for i, s0 in enumerate(stones):
    for s1 in stones[i + 1:]:
        collision = collide_ij(s0, s1)
        p1 += collision is not None and collision is not PARALLEL and all(lo <= p <= hi for p in collision)

print(f"Part one: {p1}")

def collisions_ij(di, dj):
    ij = None
    for i, s0 in enumerate(stones):
        for s1 in stones[i + 1:]:
            collision = collide_ij(s0, s1, (di, dj))
            if collision is PARALLEL:
                continue
            if collision is None:
                return None
            if ij is not None and collision != ij:
                return None
            ij = collision
    return ij

def collisions_ik(di, dk):
    ik = None
    for i, s0 in enumerate(stones):
        for s1 in stones[i + 1:]:
            collision = collide_ik(s0, s1, (di, dk))
            if collision is PARALLEL:
                continue
            if collision is None:
                return None
            if ik is not None and collision != ik:
                return None
            ik = collision
    return ik


for di in range(-256, 256):
    for dj in range(-256, 256):
        ij = collisions_ij(di, dj)
        if ij is not None:
            for dk in range(-256, 256):
                ik = collisions_ik(di, dk)
                if ik is not None:
                    print(f"Part two: {int(ij[0] + ij[1] + ik[1])}")
                    break
            break
