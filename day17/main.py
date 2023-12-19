import sys
import heapq

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

lines = data.splitlines()
grid = {i + j*1j: int(c) for i, line in enumerate(lines) for j, c in enumerate(line)}
H, W = len(lines), len(lines[0])
END = H - 1 + (W - 1)*1j

def pathfind(lo, hi):
    heap = [(0, id(d), d, d, 1) for d in (1, 1j)]
    heapq.heapify(heap)
    seen = set()

    while heap:
        a, _, p, dp, consec = heapq.heappop(heap)
        if p not in grid or consec > hi or (p, dp, consec) in seen:
            continue
        seen.add((p, dp, consec))
        a += grid[p]
        if p == END:
            return a
        heapq.heappush(heap, (a, id(p + dp), p + dp, dp, consec + 1))
        if consec >= lo:
            for ndp in (dp * 1j, dp * -1j):
                heapq.heappush(heap, (a, id(p + ndp), p + ndp, ndp, 1))

print(f"Part one: {pathfind(0, 3)}")
print(f"Part two: {pathfind(4, 10)}")
