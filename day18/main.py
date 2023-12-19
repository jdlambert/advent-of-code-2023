import sys

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

orders = [line.split() for line in data.splitlines()]

dirs = {
    "R": (0, 1),
    "L": (0, -1),
    "U": (-1, 0),
    "D": (1, 0),
}

def polygon_area(vecs):
    i, j = 0, 0
    vertices = [(0, 0)]
    perimeter = 0
    for mag, dir in vecs:
        di, dj = dirs[dir]
        perimeter += mag
        i += di * mag
        j += dj * mag
        vertices.append((i, j))

    shoelace = sum(i0*j1 - i1*j0 for (i0, j0), (i1, j1) in zip(vertices, vertices[1:]))
    return abs(shoelace // 2) + perimeter//2 + 1

p1 = polygon_area([(int(b), a) for a, b, _ in orders])

vecs = []
for _, _, code in orders:
    code = code.strip("(#)")
    mag = int(code[:5], 16)
    dir = "RDLU"[int(code[-1])]
    vecs.append((mag, dir))

p2 = polygon_area(vecs)

print(f"Part one: {p1}")
print(f"Part two: {p2}")
