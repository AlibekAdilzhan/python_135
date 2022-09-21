my_list = [
    [1, 2, 3], # 6
    [2, 3, 7], # 12
    [1, 8, 1], # 10
    [1, 1, 9]  # 11
]

s = 0

for x in my_list:
    s = sum(x)
    print(s)