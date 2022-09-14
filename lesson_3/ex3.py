a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a > 0 and b > 0 and c < 0 and d < 0:
    print("ok")
elif a > 0 and b < 0 and c > 0 and d < 0:
    print("ok")
elif a > 0 and b < 0 and c < 0 and d > 0:
    print("ok")
elif a < 0 and b > 0 and c > 0 and d < 0:
    print("ok")
elif a < 0 and b > 0 and c < 0 and d > 0:
    print("ok")
elif a < 0 and b < 0 and c > 0 and d > 0:
    print("ok")
else:
    print("oh no")

# 1 2 3 4