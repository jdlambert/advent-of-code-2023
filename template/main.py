import sys

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

p1 = 0
p2 = 0

print(f"Part one: {p1}")
print(f"Part two: {p2}")
