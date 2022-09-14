n = int(input())
a = 0
b = 1
# a b c
#   a b c
#     a b c
# 0 1 1 2 3 5 8
for i in range(n - 2):
    c = a + b
    a = b
    b = c
print(c, end=" ")