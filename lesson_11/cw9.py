set_1 = {1, 1, 2, 3, 4}
set_2 = {1, 2, 3, 4, 4}

a = set_1.pop()
print(a)
set_1.add(5)
set_1.discard(4)
print(set_1)
print(set_2)
print(set_1 == set_2)

list_1 = list(set_1)
for i in range(len(list_1)):
    print(list_1[i])

for x in set_1:
    print(x)

