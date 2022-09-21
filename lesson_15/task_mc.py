n = 8

array_2d = [list(input()) for _ in range(n)]
directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [0, 0]]
for i in range(len(array_2d)):
    for j in range(len(array_2d[i])):
        if array_2d[i][j] == "X":
            for d in directions:
                if 0 <= i + d[0] < n and 0 <= j + d[1] < n:
                    array_2d[i + d[0]][j + d[1]] = "@"

print("---------------------")

for x in array_2d:
    x = "".join(x)
    print(x)
########
##X#####
########
######X#
########
########
##X#####
########