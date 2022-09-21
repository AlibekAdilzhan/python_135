n = 3
m = 3
array_2d = [[int(x) for x in input().split()] for _ in range(n)]

array_2d = [
    [0, 1, 1],
    [3, 2, 1],
    [1, 1, 8]
]


for i in range(len(array_2d)):
    for j in range(m // 2):
        temp_value = array_2d[i][m - j - 1] # temp_value = 1
        array_2d[i][m - 1 - j] = array_2d[i][j] 
        array_2d[i][j] = temp_value

for x in array_2d:
    print(x)
