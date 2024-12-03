import re

# Open the file in read mode and process it
with open("data.txt", "r") as file:
    data = file.read()


matches = re.findall(r"mul\((\d+),(\d+)\)", data)

result = sum(int(x) * int(y) for x, y in matches)

# matches = []
# for line in data:
#     matches.extend(re.findall(r"mul\((\d+),(\d+)\)", line))

# result = 0
# for input in matches:
#     result += int(input[0])*int(input[1])

print(result)
