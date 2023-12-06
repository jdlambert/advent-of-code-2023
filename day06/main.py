import re
import sys

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

lines = data.splitlines()
_, time_line = lines[0].split(":")
_, dist_line = lines[1].split(":")
times = [int(n, 10) for n in time_line.split()]
dists = [int(n, 10) for n in dist_line.split()]

def is_valid(i: int, t: int) -> bool:
    rest = times[i] - t
    print(f"{i} {t}: {dists[i] < rest * t}")
    return dists[i] < rest * t

def valid_count(i: int) -> int:
    return len([t for t in range(times[i]) if is_valid(i, t)])

p1 = 1

for i in range(len(times)):
    p = valid_count(i)
    p1 *= p
    print(f"IIII {i}: {p}")

def extract(line: str) -> int:
    b = []

    for t in re.findall(r'\d', line):
        b.append(t)

    return int(''.join(b), 10)


times.append(extract(time_line))
dists.append(extract(dist_line))

p2 = valid_count(len(times) - 1)

print(f"Part one: {p1}")
print(f"Part two: {p2}")
