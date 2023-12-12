import sys
import functools

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

def valid_count(springs, groups):

    @functools.cache
    def count(si, gi, run):
        if si == len(springs):
            if run:
                return gi < len(groups) and groups[gi] == run and gi + 1 == len(groups)
            return gi == len(groups)
        if gi == len(groups):
            return '#' not in springs[si:]   
        potential = 0
        if springs[si] in '.?':
            if run == 0:
                potential += count(si + 1, gi, 0)
            elif run == groups[gi]:
                potential += count(si + 1, gi + 1, 0)
        if springs[si] in '#?':
            if run + 1 <= groups[gi]:
                potential += count(si + 1, gi, run + 1)
        return potential

    return count(0, 0, 0)

def compute(times):
    total = 0
    for line in data.splitlines():
        springs, groups = line.split()
        groups = [int(g) for g in groups.split(',')]
        total += valid_count("?".join([springs] * times), groups * times)
    return total

print(f"Part one: {compute(1)}")
print(f"Part two: {compute(5)}")
