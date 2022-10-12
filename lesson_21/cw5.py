import re

s = "adfs..,sadf,asfa-sdf"

pattern = r"[.,-]+"

result = re.split(pattern, s)

print(*result)