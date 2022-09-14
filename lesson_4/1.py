n = int(input())

# 1 ---> utka
# 2, 3, 4 --> utki
# rest ---> utok
# 11, 12, 13, 14 ---> utok

if 11 <= n % 100 <= 14:
    print(n, "уток")
elif n % 10 == 1:
    print(n, "утка")
elif 2 <= n % 10 <= 4:
    print(n, "утки")
else:
    print(n, "уток")