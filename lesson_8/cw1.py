s = 0
x = int(input())
y = int(input())
i = 0
while s < y:
    s = s + x
    x = x * 1.2
    i += 1

print(i) 