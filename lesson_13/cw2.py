data = dict(zip(range(7), "abcdefg"))

print(data.keys())

# for k in data.keys():
#     print(k, data[k])

# for v in data.values():
#     print(v)

# for k, v in data.items():
#     print(k, v)

for k in data:
    print(k, data[k])
for k in data.keys():
    print(k, data[k])