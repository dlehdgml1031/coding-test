from itertools import permutations, combinations

N, S = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

for i in range(1, N + 1):
    for cur in combinations(arr, i):
        if sum(cur) == S:
            ans += 1
   
print(ans)