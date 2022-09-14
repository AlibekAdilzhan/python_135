age = int(input("Enter age: "))
friends_number = int(input("Enter fn: "))

s1 = "My age is {0}, I have {1} friends".format(age, friends_number)
s2 = f"My age is {age}, I have {friends_number} friends"
s3 = "My age is %d, I have %d friends and my name is %s" % (age, friends_number, "Jack")
# s4 = "Your company costs %2d" % 22
s4 = f"{age:04d}"

print(s1)
print(s2)
print(s3)
print(s4)

# 001
# 002 