l1 = set(input())
l2 = set()
for x in l1:
    if x.isalpha():
        l2.add(x)
s = list(l2)
s.sort()
s.reverse()
r = " ".join(s)
print(r)