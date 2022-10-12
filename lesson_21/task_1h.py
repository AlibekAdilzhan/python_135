import re 

s = "87025122449"

pattern = r"^(\+?7|\+?8)?\s?\(?(\d{3})\)?\s?(\d{3})\s?(\d{2})-?(\d{2})"

result = re.search(pattern, s)

if result is not None:
    result_string = f"+7 ({result.group(2)}) {result.group(3)} {result.group(4)}-{result.group(5)}"
    print(result_string)
else:
    print("ne nashel")