seconds = int(input())

hour = seconds // 60 // 60
minutes = seconds // 60 % 60
seconds = seconds % 60

print(hour, minutes, seconds)