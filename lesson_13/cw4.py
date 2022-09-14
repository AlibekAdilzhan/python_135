info_m = {
    "name": "Aidana",
    "grades": [96, 78, 67, 59, 98, 76]
}

s = 0
for r in info_m["grades"]:
    s += r
s /= len(info_m["grades"])
print(s)