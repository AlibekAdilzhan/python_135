L = int(input())
R = int(input())
# 9 7 5 3
if L % 2 == 0:
    L = L - 1
print("_________")
for i in range(L, R - 1, -2):
    print(i, end=" ")