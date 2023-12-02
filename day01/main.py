import re

mapping = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

def parse(match: str) -> int:
    try:
        return int(match, 10)
    except:
        return 1 + mapping.index(match)

with open("input.txt") as f:
    data = f.read()

lines = data.splitlines()

part1 = 0
part2 = 0

for line in lines:
    nums = re.findall(r'\d', line)
    part1 += 10 * int(nums[0], 10) + int(nums[-1], 10)
    p2nums = re.findall(rf'(?=(\d|{"|".join(mapping)}))', line)
    part2 += 10 * parse(p2nums[0]) + parse(p2nums[-1])


print(f"Part one: {part1}")
print(f"Part two: {part2}")
