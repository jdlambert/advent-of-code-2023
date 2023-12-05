with open("input.txt") as f:
    data = f.read()

sections = data.split("\n\n")
seed_section, *rest = sections
_, seed_list = seed_section.split(":")
seeds = [int(n, 10) for n in seed_list.split()]

class Transformer:
    def __init__(self, section: str):
        self.title, *ranges = section.splitlines()
        self.tuples = []
        for r in ranges:
            a, b, c = r.split()
            self.tuples.append((int(b), int(a), int(c)))
        self.tuples.sort()

    def transform(self, seed: int, seed_count: int) -> [(int, int)]:
        for l, r, range_count in self.tuples:
            if l <= seed < l + range_count:
                if seed_count <= range_count - (seed - l):
                    return [(r + (seed - l), seed_count)]
                consumed = range_count - (seed - l)
                return [(r + (seed - l), consumed)] + self.transform(seed + consumed, seed_count - consumed)
        for l, _, _ in self.tuples:
            if seed < l < seed + seed_count:
                consumed = (l - seed)
                return [(seed, consumed)] + self.transform(seed + consumed, seed_count - consumed)
        return [(seed, seed_count)]

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

p1 = float("inf")
p2 = float("inf")

for seed in seeds:
    locs = seeds_to_locs(seed, 1)
    min_loc = min(locs, key=lambda x: x[0])[0]
    p1 = min(min_loc, p1)

for i in range(len(seeds) // 2):
    start = seeds[2 * i]
    count = seeds[2*i + 1]
    locs = seeds_to_locs(start, count)
    min_loc = min(locs, key=lambda x: x[0])[0]
    p2 = min(min_loc, p2)

print(f"Part one: {p1}")
print(f"Part two: {p2}")
