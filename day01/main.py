import re

with open("input.txt") as f:
    data = f.read()

lines = data.splitlines()

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

def extract(regex: str) -> int:
    total = 0
    for line in lines:
        nums = re.findall(regex, line)
        total += 10 * parse(nums[0]) + parse(nums[-1])
    return total

p1 = extract(r'\d')
print(f"Part one: {p1}")
p2 = extract(rf'(?=(\d|{"|".join(mapping)}))')
print(f"Part two: {p2}")
