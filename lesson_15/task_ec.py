n = int(input())
array_2d = [[int(x) for x in input().split()] for _ in range(n)]
s = 0
for x in array_2d:
    for y in x:
        if y < 0:
            s += 1
print(s)