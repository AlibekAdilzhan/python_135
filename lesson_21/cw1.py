import re

s = """
Astana
Almaty
Karagandy
Uskaman
Semei
Aktau
Atyrau
Kokshetau
"""

pattern = r"A\w+"
result = re.findall(pattern, s)
print(result)