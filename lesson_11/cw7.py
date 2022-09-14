from operator import is_

#         012345678    n = 9,
my_str = "gobojobog" #  9 // 2 = 4

n = len(my_str)
#
m = n // 2 # 5 // 2 = 2
is_polindrome = True
for i in range(m):
    if my_str[i] != my_str[(n - 1) - i]:
        is_polindrome = False
        break

if is_polindrome == True:
    print("polindrome")
else:
    print("not polindrome")
