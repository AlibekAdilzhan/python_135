# s = input()
# ordered_s = sorted(s) # ["a", "b", "c"] # O(nlog(n))
# ordered_s = "".join(ordered_s) # "abc"
# if ordered_s == s:
#     print("good")
# else:
#     print("cringe")


# O(n)
print("enter new task")

s = input()
i = 0
asc = ord(min(s))
ordered = True
while i < len(s):
    if asc != ord(s[i]):
        ordered = False
        break
    #print(s[i])
    asc += 1
    i += 1
    
if ordered == False:
    print("Cringe")
else:
    print("Good")