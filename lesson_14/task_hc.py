# a, aa, aab, aac, aacde
l = input().split()

d = {}
dr = {}
# dr = {3: ["abc", "adc", "aaa"]}
for x in l:
    length = len(x)
    d[x] = length
    if length not in dr:
        dr[length] = [x]
    else:
        dr[length].append(x)

sorted_l = []
dr_keys = list(dr.keys())

for i in range(len(dr_keys) - 1, -1, -1):
    k = dr_keys[i]
    one_list = sorted(dr[k])
    sorted_l.extend(one_list)
print(sorted_l)