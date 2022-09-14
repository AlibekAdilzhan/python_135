print("enter number")
a = int(input())
b = int(input())
for i in range(1, a + 1):
    s=(i*b)
    if s % a == 0:
        print(s)
        break