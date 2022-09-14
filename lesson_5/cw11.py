n = 10234

s = 0

while True:
    a = n % 10
    s = s + a
    n = n // 10
print(s)