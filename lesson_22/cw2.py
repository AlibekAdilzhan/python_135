import os

with open("cities.txt", "r") as fo:
    lines = fo.readlines()

print(lines)

with open("cities.txt", "w") as fo:
    for x in lines:
        if len(x) > 6 and x[5] != "e":
            fo.write(x)
