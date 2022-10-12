import re

s = "f@abcefg.kz"

pattern = r"[0-9a-z\._]+@[a-z]{2,6}\.[a-z]{2,4}"

result = re.search(pattern, s)

print(result)