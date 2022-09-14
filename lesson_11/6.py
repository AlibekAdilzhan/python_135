
s1 = set()
s2 = set()

x = int(input())
for _ in range(x):
    name = input()
    s1.add(name)

y = int(input())
for _ in range(y):
    name = input()
    s2.add(name)

abs = s2 - s1
imp = s1 - s2
print(abs)
print(imp)