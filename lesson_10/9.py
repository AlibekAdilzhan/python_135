
#    012345
s = "abcdefg"
# len(s) // 2

s2 = s[len(s) // 2 : ]
s1 = s[ : len(s) // 2]

s_new = s1 + s2.upper()

print(s_new)