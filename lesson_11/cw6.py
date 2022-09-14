s = input()
my_count_lower = 0
my_count_upper = 0

for i in range(len(s)):
    if s[i].islower():
        my_count_lower += 1
    else:
        my_count_upper += 1
e = my_count_lower*my_count_upper
print(e)