with open("input.txt") as f:
    data = f.read()

lines = data.splitlines()

p1 = 0

wins = dict()
counts = dict()

def count(i):
    if i not in counts:
        total = 1
        for j in range(wins[i]):
            total += count(i + j + 1)
        counts[i] = total
    return counts[i]

for line in lines:
    title, cards = line.split(":")
    _, num = title.split()
    winners, mine = cards.split("|")
    winning_nums = {int(n, 10) for n in winners.split()}
    my_nums = {int(n, 10) for n in mine.split()}
    matches = my_nums.intersection(winning_nums)
    if matches:
        p1 += 2 ** (len(matches) - 1)
    wins[int(num, 10)] = len(matches)

p2 = sum(count(i + 1) for i in range(len(lines)))

print(f"Part one: {p1}")
print(f"Part two: {p2}")
