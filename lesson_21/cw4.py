import re

s = "Im 18 years old hi 43"

pattern = r"\d+"

result = re.sub(pattern, "", s)
print(result)
