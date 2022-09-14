l = list(map(int, input().split()))
n = int(input())


for i in range(len(l) - 1):
    for j in range(i + 1, len(l)):
        if l[i] + l[j] == n:
            print(l[i], l[j])