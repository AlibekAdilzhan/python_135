from cgitb import reset
import re

s = "+77711088121"

pattern = r"(\+7|8)(\d{3})(\d{7})"
result = re.search(pattern, s)
print(result.group(2))
