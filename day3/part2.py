import re

with open("data.txt", "r") as file:
    data = file.read()

mul_pattern = r"mul\((\d+),(\d+)\)"
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"

enabled = True
result = 0

instructions = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", data)

for instruction in instructions:
    if re.fullmatch(do_pattern, instruction):
        enabled = True
    elif re.fullmatch(dont_pattern, instruction):
        enabled = False
    elif enabled and re.fullmatch(mul_pattern, instruction):
        x, y = map(int, re.findall(r"\d+", instruction))
        result += x * y

print(result)
