n = int(input())
d = {}
for _ in range(n):
    x = input().split()
    name = x[0]
    score = int(x[1])
    if name not in d.keys():
        d[name] = score
    else:
        if d[name]<score:
            d[name]=score


for y in d.keys():
    print(f"{y}:{d[y]}")