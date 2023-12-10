import sys

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

seqs = [[int(n) for n in seq.split()] for seq in data.splitlines()]

def predict(seq: list[int]) -> int:
    l = r = 0
    l_sign = 1

    while any(n != 0 for n in seq):
        l += l_sign * seq[0]
        l_sign *= -1
        r += seq[-1]
        seq = [b - a for a, b in zip(seq, seq[1:])]
    
    return l, r

preds = [predict(s) for s in seqs]

p1 = sum(pred[1] for pred in preds)
p2 = sum(pred[0] for pred in preds)

print(f"Part one: {p1}")
print(f"Part two: {p2}")
