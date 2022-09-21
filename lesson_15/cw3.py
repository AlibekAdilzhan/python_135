my_list = []
n = 3
m = 4

for i in range(n):
    row = [0] * m
    my_list.append(row)

for row in my_list:
    print(row)
print("-----------------")
my_list[1][2] = 5
for row in my_list:
    print(row)
