N, M = map(int, input().split())

App = list(map(int, input().split()))
Cost = list(map(int, input().split()))

total_cost = sum(Cost)

dp = [0] * (total_cost + 1)

for i in range(N):
    for c in range(total_cost, Cost[i] - 1, -1):
        dp[c] = max(dp[c], dp[c - Cost[i]] + App[i])

for c in range(total_cost + 1):
    if dp[c] >= M:
        print(c)
        break