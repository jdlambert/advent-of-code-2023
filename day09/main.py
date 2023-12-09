import sys

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

seqs = [[int(n) for n in seq.split()] for seq in data.splitlines()]

def predict(seq: list[int]) -> int:
    cur = seq
    finals = []
    initials = []
    initial_sign = 1
    while any(n != 0 for n in cur):
        finals.append(cur[-1])
        initials.append(initial_sign * cur[0])
        initial_sign *= -1
        cur = [b - a for a, b in zip(cur, cur[1:])]
    
    return sum(finals), sum(initials)

preds = [predict(s) for s in seqs]

p1 = sum(pred[0] for pred in preds)
p2 = sum(pred[1] for pred in preds)

print(f"Part one: {p1}")
print(f"Part two: {p2}")
