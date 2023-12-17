import sys

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

inputs = data.replace('\n', '').split(',')

def hash(s):
    h = 0
    for c in s:
        h += ord(c)
        h *= 17
        h %= 256
    return h

p1 = sum(hash(s) for s in inputs)

boxes = [[] for _ in range(256)]

lenses = []
for i in inputs:
    if '=' in i:
        lenses.append((int(i[-1]), i[:-2]))
    else:
        lenses.append((0, i[:-1]))

for op, s in lenses:
    box = boxes[hash(s)]
    if op:
        for i, (l, p) in enumerate(box):
            if l == s:
                box[i] = (s, op)
                break
        else:
            box.append((s, op))
    else:
        for i, (l, p) in enumerate(box):
            if l == s:
                box.pop(i)
                break

def focal(i, box):
    s = 0
    for j, (_, l) in enumerate(box):
        s += (1 + i) * (1 + j) * l
    return s


p2 = sum([focal(*b) for b in enumerate(boxes)])

print(f"Part one: {p1}")
print(f"Part two: {p2}")
