import re 

s = input()

pattern = r"(d|D)(e|E)(c|C)(o|O)(d|D)(e|E)"

result = re.search(pattern, s)
if result is None:
    print("ne nahsel")
else:
    print(result.start(),result.end())