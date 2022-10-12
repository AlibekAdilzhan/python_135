import re 

s = "the 9th of June"
# therefore
pattern = r"^(The|the) "

result = re.search(pattern, s)
print(result.start(), result.end())