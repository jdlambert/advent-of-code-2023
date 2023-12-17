import sys
import heapq

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

grid = [[int(c) for c in line] for line in data.splitlines()]

N, E, S, W = (-1, 0), (0, 1), (1, 0), (0, -1)

def in_bounds(i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

def turn(dir):
    return {
        N: [N, E, W],
        W: [N, S, W],
        S: [E, W, S],
        E: [N, S, E],
    }[dir]

def pathfind(lo, hi):
    heap = [(0, (d[0], d[1]), d, 1) for d in (E, S)]
    heapq.heapify(heap)
    seen = set()

    while heap:
        heat, pos, d, consec = heapq.heappop(heap)
        if consec > hi:
            continue
        if not in_bounds(*pos):
            continue
        if (pos, d, consec) in seen:
            continue
        seen.add((pos, d, consec))
        heat += grid[pos[0]][pos[1]]
        if pos == (len(grid) - 1, len(grid[0]) - 1):
            return heat
        if consec < lo:
            heapq.heappush(heap, (heat, (pos[0] + d[0], pos[1] + d[1]), d, consec + 1))
        else:
            for t in turn(d):
                heapq.heappush(heap, (heat, (pos[0] + t[0], pos[1] + t[1]), t, consec + 1 if t == d else 1))

print(f"Part one: {pathfind(0, 3)}")
print(f"Part two: {pathfind(4, 10)}")
