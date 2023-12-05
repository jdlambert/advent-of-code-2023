import bisect

with open("input.txt") as f:
    data = f.read()

sections = data.split("\n\n")
seed_section, *rest = sections
_, seed_list = seed_section.split(":")
seeds = [int(n, 10) for n in seed_list.split()]

class Transformer:
    def __init__(self, section: str):
        _, *ranges = section.splitlines()
        self.tuples = []
        for r in ranges:
            a, b, c = r.split()
            self.tuples.append((int(b), int(a), int(c)))
        self.tuples.sort()

    def transform(self, seed: int, seed_count: int) -> [(int, int)]:
        i = bisect.bisect(self.tuples, seed, key=lambda x: x[0])
        if i > 0: # Check if we're in the previous range
            l, r, range_count = self.tuples[i - 1]
            if l <= seed < l + range_count:
                if seed_count <= range_count - (seed - l):
                    return [(r + (seed - l), seed_count)]
                consumed = range_count - (seed - l)
                return [(r + (seed - l), consumed)] + self.transform(seed + consumed, seed_count - consumed)
        if i < len(self.tuples): # Check if the next range overlaps
            l, _, _ = self.tuples[i]
            if seed < l < seed + seed_count:
                consumed = (l - seed)
                return [(seed, consumed)] + self.transform(seed + consumed, seed_count - consumed)
        return [(seed, seed_count)] # The seed range overlaps no ranges

    def transform_many(self, seed_ranges: [(int, int)]) -> [(int, int)]:
        out = []
        for s, sc in seed_ranges:
            out.extend(self.transform(s, sc))
        return out

maps = [Transformer(s) for s in rest]

def seeds_to_locs(seed: int, seed_count: int) -> [(int, int)]:
        cur = [(seed, seed_count)]
        for m in maps:
            cur = m.transform_many(cur)
        return cur

def min_loc(seed_pairs: [(int, int)]) -> int:
    m = float("inf")
    for seed, count in seed_pairs:
        locs = seeds_to_locs(seed, count)
        min_loc = min(locs, key=lambda x: x[0])[0]
        m = min(min_loc, m)
    return m

p1 = min_loc([(seed, 1) for seed in seeds])
print(f"Part one: {p1}")

p2 = min_loc([
    (seeds[2 * i], seeds[2*i + 1]) for i in range(len(seeds) // 2)
])
print(f"Part two: {p2}")
