n = int(input())

a = n % 10 # last
b = (n // 10) % 10 # middle
c = n // 100 # first

print(a + b + c)