a = float(input())
symbol = input() # "+" "-" "*"...
b = float(input())

if symbol == "+":
    print(a + b)
elif symbol == "-":
    print(a - b)
elif symbol == "*":
    print(a * b)
elif symbol == "/":
    if b == 0:
        print("zero division error")
    else:
        print(a / b)
elif symbol == "**":
    print(a**b)
elif symbol == "//":
    print(a // b)
elif symbol == "%":
    print(a % b)
else:
    print("your symbol is incorrect")