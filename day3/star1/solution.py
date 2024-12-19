import re

with open("input.txt", "r") as file:
    input = file.read()
matches = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", input)
sum = 0
for match in matches:
    leftParIndex = match.find("(")
    commaIndex = match.find(",")
    rightParIndex = match.find(")")
    arg1 = match[leftParIndex + 1 : commaIndex]
    arg2 = match[commaIndex + 1 : rightParIndex]
    sum += int(arg1) * int(arg2)
print(sum)
