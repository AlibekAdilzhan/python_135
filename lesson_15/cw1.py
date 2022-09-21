my_list = [
    [1, 2, 3],
    [2, 3, 7],
    [1, 8, 1],
    [1, 1, 9]
]

for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        print(my_list[i][j], end=" ")
    print()

for x in my_list:
    for y in x:
        print(y, end=" ")
    print()