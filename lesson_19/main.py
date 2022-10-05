from module import detroid

s = input()
c = detroid(s) # {"a": 3, "b": 1, "c":5, "d": 1}
for k in c.keys():
    print(f"{k}: {c[k]}")