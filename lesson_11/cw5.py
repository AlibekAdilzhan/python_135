my_str = input()
result_str = ""

for c in my_str:
    if c.islower():
        result_str += c.upper()
    else:
        result_str += c.lower()

print(result_str)
