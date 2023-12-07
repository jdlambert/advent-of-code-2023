import sys
import collections

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

lines = data.splitlines()
hand_splits = [line.split() for line in lines]
hands = [(hand, int(bid, 10)) for (hand, bid) in hand_splits]

strengths = [
    "A", 
    "K",
    "Q",
    "J",
    "T",
    "9",
    "8",
    "7",
    "6",
    "5",
    "4",
    "3",
    "2",
]

p2_strengths = [
    "A", 
    "K",
    "Q",
    "T",
    "9",
    "8",
    "7",
    "6",
    "5",
    "4",
    "3",
    "2",
    "J",
]

def label_str(hand: str):
    counts = list(collections.Counter(hand).values())
    counts.sort(reverse=True)
    if counts[0] == 5: return 0
    if counts[0] == 4: return 1
    if counts[0] == 3:
        if counts[1] == 2: return 2
        return 3
    if counts[0] == 2:
        if counts[1] == 2: return 4
        return 5
    return 6

def p2_label_str(hand: str):
    counts = collections.Counter(hand)
    j = counts.pop("J") if "J" in counts else 0
    counts = list(counts.values())
    counts.sort(reverse=True)
    if counts:
        counts[0] = counts[0] + j
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

def p2_tiebreak_str(hand):
    return [p2_strengths.index(card) for card in hand]
     
p1 = 0
hands.sort(key=lambda h: (label_str(h[0]), *tiebreak_str(h[0])), reverse=True)
for rank, (_, bid) in enumerate(hands):
    p1 += (rank + 1) * bid

p2 = 0
hands.sort(key=lambda h: (p2_label_str(h[0]), *p2_tiebreak_str(h[0])), reverse=True)
for rank, (_, bid) in enumerate(hands):
    p2 += (rank + 1) * bid

print(f"Part one: {p1}")
print(f"Part two: {p2}")