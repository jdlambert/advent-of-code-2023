import sys
import collections

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

lines = data.splitlines()
hand_splits = [line.split() for line in lines]
hands = [(hand, int(bid, 10)) for (hand, bid) in hand_splits]

strengths = "AKQJT98765432"

def label_str(hand: str, wild: bool = False):
    counts = collections.Counter(hand)
    if wild:
        j = counts.pop("J") if "J" in counts else 0
    counts = list(counts.values())
    counts.sort(reverse=True)
    if wild:
        if counts:
            counts[0] += j
        else:
            counts.append(j)
    if counts[0] == 5: return 0
    if counts[0] == 4: return 1
    if counts[0] == 3:
        if counts[1] == 2: return 2
        return 3
    if counts[0] == 2:
        if counts[1] == 2: return 4
        return 5
    return 6

def tiebreak_str(hand):
    return [strengths.index(card) for card in hand]

p1 = 0
hands.sort(key=lambda h: (label_str(h[0]), *tiebreak_str(h[0])), reverse=True)
for rank, (_, bid) in enumerate(hands):
    p1 += (rank + 1) * bid

p2 = 0
strengths = strengths.replace('J', '') + 'J'
hands.sort(key=lambda h: (label_str(h[0], True), *tiebreak_str(h[0])), reverse=True)
for rank, (_, bid) in enumerate(hands):
    p2 += (rank + 1) * bid

print(f"Part one: {p1}")
print(f"Part two: {p2}")
