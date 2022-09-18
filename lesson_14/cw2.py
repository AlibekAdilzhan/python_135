l = list(map(int, input().split()))
s = sum(l)
if s > 10:
    print("more")
elif s < 10:
    print("less")
else:
    print("equal")