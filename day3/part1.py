import re

# Open the file in read mode and process it
with open("data.txt", "r") as file:
    # Read all lines from the file
    data = file.readlines()

matches = []

for line in data:
    matches.extend(re.findall(r"mul\((\d+),(\d+)\)", line))

result = 0
for input in matches:
    result += int(input[0])*int(input[1])

print(result)
