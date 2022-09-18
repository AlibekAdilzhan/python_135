l = input().split()
l_sorted = sorted(l, key=lambda x: len(x), reverse=True)
print(l_sorted)