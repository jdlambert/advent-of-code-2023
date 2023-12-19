import sys
import re

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

workflows, parts = data.split("\n\n")

NEXT = "next"

class Rule:
    def __init__(self, s):
        if ":" in s:
            self.pred, self.result = s.split(":")
            key = self.pred[0]
            val = int(self.pred[2:])
            if self.pred[1] == '<':
                self.test = lambda p: p[key] < val
            else:
                self.test = lambda p: p[key] > val
        else:
            self.pred = ''
            self.result = s
            self.test = lambda _: True

    def process(self, p):
        if self.test(p):
            return self.result
        return NEXT

class Workflow:
    def __init__(self, s):
        self.name, rules = s.strip("}").split("{")
        self.rules = [Rule(s) for s in rules.split(',')]
    
    def process(self, p):
        for rule in self.rules:
            r = rule.process(p)
            if r == 'A': return True
            if r == 'R': return False
            if r != NEXT: return wfs[r].process(p)

wfs = [Workflow(l) for l in workflows.splitlines()]
wfs = {wf.name: wf for wf in wfs}
ps = []
for line in parts.splitlines():
    p = {}
    for k, v in zip("xmas", re.findall("\d+", line)):
        p[k] = int(v)
    ps.append(p)

p1 = sum([sum(p.values()) for p in ps if wfs["in"].process(p)])

frontier = [('in', [])]
accepts = []

while frontier:
    w, c = frontier.pop()
    wf = wfs[w]
    for rule in wf.rules:
        if rule.pred:
            if rule.result == 'A':
                accepts.append(c + [rule.pred])
            elif rule.result != 'R':
                frontier.append((rule.result, c + [rule.pred]))
            c.append("!" + rule.pred)
        else:
            if rule.result == 'A':            
                accepts.append(c)
            elif rule.result != 'R':
                frontier.append((rule.result, c))

def join(accept):
    ranges = {
        "x": (1, 4000),
        "m": (1, 4000),
        "a": (1, 4000),
        "s": (1, 4000),
    }

    for constraint in accept:
        neg = constraint.startswith("!")
        constraint = constraint.strip("!")
        key = constraint[0]
        sym = constraint[1]
        val = int(constraint[2:])
        lo, hi = ranges[key]
        if sym == '<':
            if neg:
                lo = max(val, lo)
            else:
                hi = min(val - 1, hi)
        else:
            if neg:
                hi = min(val, hi)
            else:
                lo = max(val + 1, lo)
        ranges[key] = (lo, hi)

    return ranges

def count_admissions(a):
    p = 1
    for (i, j) in join(a).values():
        p *= max(j - i + 1, 0)
    return p

p2 = sum(count_admissions(a) for a in accepts)

print(f"Part one: {p1}")
print(f"Part two: {p2}")
