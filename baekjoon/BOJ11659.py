N, M = map(int, input().split())

arr = [0] + list(map(int, input().split()))
idx = [list(map(int, input().split())) for _ in range(M)]

p_sum = [0] * (N + 1)

for i in range(1, N + 1):
    p_sum[i] = p_sum[i - 1] + arr[i]
    
for i, j in idx:
    print(p_sum[j] - p_sum[i - 1])