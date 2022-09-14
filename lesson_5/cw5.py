n = int(input())
s = 0
i = 1

# 1 + 2 + 3 + 4 + 5 + 6
# s = s + 1 ---> s = 1
# s = s + 2 ---> s = 3
# s = s + 3 ---> s = 6

# Grokking algorithms 

while i <= n: # O(n)
    s += i
    i += 1

print(s)