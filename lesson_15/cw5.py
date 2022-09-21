n = 3 # row number
m = 4 # column number

my_list = [[0] * m] * n # tak nel'za
array = [[0] * m for _ in range(n)] # nado vot tak

array[1][2] = 5

for x in array:
    print(x)