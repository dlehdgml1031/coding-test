from collections import defaultdict

hs = defaultdict(int)

N = int(input())
n_arr = list(map(int, input().split()))

M = int(input())
m_arr = list(map(int, input().split()))

for x in n_arr:
    hs[x] += 1

for x in m_arr:
    if hs[x]:
        print(1)
    else:
        print(0)