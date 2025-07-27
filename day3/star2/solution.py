import re

with open("input.txt", "r") as file:
    input = file.read()
matches = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)", input)
# print(matches)
sum = 0
enabled = True
for match in matches:
    if match == "don't()":
        enabled = False
    elif match == "do()":
        enabled = True
    else:
        if enabled:
            leftParIndex = match.find("(")
            commaIndex = match.find(",")
            rightParIndex = match.find(")")
            arg1 = match[leftParIndex + 1 : commaIndex]
            arg2 = match[commaIndex + 1 : rightParIndex]
            sum += int(arg1) * int(arg2)
print(sum)
