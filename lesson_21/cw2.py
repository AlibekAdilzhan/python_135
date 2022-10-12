import re

with open("files/telephone_numbers.txt", "r") as fo:
    lines = fo.readlines()

lines = [x.strip() for x in lines]

d = {}

with open("operators.txt", "r") as fo:
    operators = fo.readlines()

operators = [x.strip() for x in operators]
for line in operators:
    line = line.split()
    print(line)
    # d["747"] = "Tele2"
    d[line[0]] = line[1]

pattern = r"(\+7|8)(\d{3})(\d{7})"

for telephone_number in lines:
    result = re.search(pattern, telephone_number)
    triples = result.group(2)
    print(telephone_number, d[triples])

# print(lines)