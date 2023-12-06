import re
import sys
import math

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

lines = data.splitlines()
_, time_line = lines[0].split(":")
_, dist_line = lines[1].split(":")
times = [int(n, 10) for n in time_line.split()]
dists = [int(n, 10) for n in dist_line.split()]

def valid_count(t: int, d: int) -> int:
    hi = math.ceil((t + math.sqrt(t ** 2 - 4 * d)) / 2)
    lo = math.floor((t - math.sqrt(t ** 2 - 4 * d)) / 2)
    return hi - lo - 1

p1 = 1

for t, d in zip(times, dists):
    p = valid_count(t, d)
    p1 *= p

def extract(line: str) -> int:
    b = []

    for t in re.findall(r'\d', line):
        b.append(t)

    return int(''.join(b), 10)

p2 = valid_count(extract(time_line), extract(dist_line))

print(f"Part one: {p1}")
print(f"Part two: {p2}")
