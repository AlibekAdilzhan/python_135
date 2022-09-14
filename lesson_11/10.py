sample_dict = {
    "Physics" : 82,
    "Math" : 65,
    "History" : 75
}

a = 1e10
mini_key = None
for k in sample_dict:
    if a > sample_dict[k]:
        a = sample_dict[k]
        mini_key = k

print(mini_key, a)