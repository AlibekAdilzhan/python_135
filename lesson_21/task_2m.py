import re 

s = "https://you.com"

pattern = r"^(http://|https://)"

result = re.search(pattern, s)

if result is None:
    print("ne nashel")
else:
    print("Found")