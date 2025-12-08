from collections import defaultdict
n = int(input())
hs = defaultdict(list)

for i in range(n):
    age, name = input().split()
    hs[i] = [int(age), name]

hs = sorted(hs.items(), key = lambda x: (x[1][0], x[0]))

for k in hs:
    print(k[1][0], k[1][1])
