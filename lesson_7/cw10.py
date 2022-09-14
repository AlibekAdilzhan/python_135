a = 1
b = 100
x = 7

for i in range(a, b + 1):
    s = 0
    j = i
    while True:
        s = s + j % 10
        j = j // 10
        if j == 0:
            break
    if s == x:
        print(i, end=" ")