print("enter words")

l = input().split()
d = {}

for i in range(len(l)):
    #l[i], len(l[i])
    d[l[i]] = len(l[i])
for k in d.keys():
    print(f"{k}-{d[k]}")