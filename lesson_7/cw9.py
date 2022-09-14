print("enter number")
a = int(input())
is_prime = True
for i in range(2, a):
    if a % i == 0:
        is_prime = False
        break

if is_prime == True:
    print("prime")
else:
    print("common")
