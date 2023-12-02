with open("input.txt") as f:
    data = f.read()

lines = data.splitlines()

limits = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

p1 = 0

for i, line in enumerate(lines):
    _, movelist = line.split(":")
    valid = True
    for move in movelist.split(";"):
        for submove in move.split(","):
            num, color = submove.strip().split(" ")
            if int(num, 10) > limits[color]:
                valid = False
    if valid:
        p1 += i + 1

p2 = 0

for i, line in enumerate(lines):
    _, movelist = line.split(":")
    maxes = {"red": 0, "green": 0, "blue": 0}
    for move in movelist.split(";"):
        for submove in move.split(","):
            num, color = submove.strip().split(" ")
            maxes[color] = max(maxes[color], int(num, 10))
    p2 += maxes["red"] * maxes["green"] * maxes["blue"]

print(f"Part one: {p1}")
print(f"Part two: {p2}")