import re

s = "Whatever it Takes Imagine dragons"

pattern = r"[A-Z]\w+"

result = re.findall(pattern, s)

print(result)