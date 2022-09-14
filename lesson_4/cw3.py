n = int(input())

a = (n // 10000000) % 100

if a == 27:
    print("Activ")
elif a == 0 or a == 8:
    print("Altel 4G")
elif a == 5 or a == 71 or a == 76 or a == 77:
    print("Beeline")
elif a == 1 or a == 2 or a == 75 or a == 78:
    print("Kcell")
elif a == 7 or a == 47:
    print("Tele2")