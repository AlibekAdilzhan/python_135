left = int(input())
right = int(input())

i = left
print("---------------------")
while i <= right:
    if i % 2 != 0:
        print(i)
    i += 1