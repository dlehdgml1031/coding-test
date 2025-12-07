from itertools import combinations

L, C = map(int, input().split())
arr = list(input().split())
arr = sorted(arr)

for comb in combinations(arr, L):
    cnt1 = 0
    cnt2 = 0
    for u in comb:
        if u in ['a', 'e', 'i', 'o', 'u']:
            cnt1 += 1
        else:
            cnt2 += 1

    if cnt1 >= 1 and cnt2 >= 2:
        print(*comb, sep = '')
    else:
        continue