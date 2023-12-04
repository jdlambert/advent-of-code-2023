with open("input.txt") as f:
    data = f.read()

lines = data.splitlines()

p1 = 0
p2 = 0

queue = []
wins = dict()

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
    queue.append(int(num, 10))

while queue:
    num = queue.pop()
    p2 += 1
    for i in range(num + 1, num + wins[num] + 1):
        queue.append(i)

print(f"Part one: {p1}")
print(f"Part two: {p2}")
