a = int(input())
s = 0
for i in range(a):
    n = int(input())
    m = n
    counter = 0
    while m > 0:
        if m % 10 == 0:
            counter += 1
        m = m // 10
    s += counter
print(s)