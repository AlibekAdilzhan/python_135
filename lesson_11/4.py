names = input().split()
names_unique = set(names)

print(len(names) - len(names_unique))