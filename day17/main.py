import sys
import heapq

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

grid = [[int(c) for c in line] for line in data.splitlines()]

dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def pathfind(lo, hi):
    heap = [(len(grid) + len(grid[0]) - 3, (d[0], d[1]), d, 1) for d in dirs[:2]]
    heapq.heapify(heap)
    seen = set()

    while heap:
        a, (i, j), (di, dj), consec = heapq.heappop(heap)
        if consec > hi:
            continue
        if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
            continue
        if ((i, j), (di, dj), consec) in seen:
            continue
        seen.add(((i, j), (di, dj), consec))
        a += grid[i][j]
        if (i, j) == (len(grid) - 1, len(grid[0]) - 1):
            return a
        heapq.heappush(heap, (a - di - dj, (i + di, j + dj), (di, dj), consec + 1))
        if consec >= lo:
            for ndi, ndj in [(ndi, ndj) for (ndi, ndj) in dirs if (ndi, ndj) not in [(-di, -dj), (di, dj)]]:
                heapq.heappush(heap, (a - ndi - ndj, (i + ndi, j + ndj), (ndi, ndj), 1))

print(f"Part one: {pathfind(0, 3)}")
print(f"Part two: {pathfind(4, 10)}")
