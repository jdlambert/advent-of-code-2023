import sys

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

grids = [group.splitlines() for group in data.split("\n\n")]

def is_h_reflection(grid, i, smudge):
    lo, hi = i - 1, i
    while lo >= 0 and hi < len(grid):
        for a, b in zip(grid[lo], grid[hi]):
            if a != b:
                smudge -= 1
                if smudge < 0:
                    return False
        lo -= 1
        hi += 1
    return smudge == 0

def is_v_reflection(grid, j, smudge):
    lo, hi = j - 1, j
    while lo >= 0 and hi < len(grid[0]):
        for line in grid:
            if line[lo] != line[hi]:
                smudge -= 1
                if smudge < 0:
                    return False
        lo -= 1
        hi += 1
    return smudge == 0

def reflect(grid, smudge):
    for i in range(1, len(grid)):
        if is_h_reflection(grid, i, smudge):
            return 100 * i
    for j in range(1, len(grid[0])):
        if is_v_reflection(grid, j, smudge):
            return j

p1, p2 = (sum(reflect(grid, s) for grid in grids) for s in (0, 1))

print(f"Part one: {p1}")
print(f"Part two: {p2}")
