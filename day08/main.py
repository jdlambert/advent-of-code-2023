import sys
import collections
import itertools
import math

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

rls, node_section = data.split("\n\n")
node_lines = node_section.splitlines()

nodes = {}
for line in node_lines:
    source = line[:3]
    nodes[source] = {"L": line[7:10], "R": line[12:15]}

def cycle_len(node: str, finished) -> int:
    for i, rl in enumerate(itertools.cycle(rls)):
        if finished(node):
            return i
        node = nodes[node][rl]

p1 = cycle_len("AAA", lambda x: x == "ZZZ")
print(f"Part one: {p1}")

# the following is valid because each Z defines a disjoint cycle
# each A is attached to one of these cycles
# A => Z len is the same as cycle len
# cycle_len(Z) % len(rls) == 0 for every Z
p2 = math.lcm(*[cycle_len(start, lambda x: x[-1] == "Z") for start in nodes if start[-1] == "A"])
print(f"Part two: {p2}")
