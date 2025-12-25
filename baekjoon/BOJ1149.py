N = int(input())
price = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * 3 for _ in range(N)]

# Initialize
for i in range(3):
    dp[0][i] = price[0][i]

# # Bottom-up DP
for y in range(1, N):
    for x in range(3):
        if x == 0:
            dp[y][x] = price[y][x] + min(dp[y-1][1], dp[y-1][2])
        elif x == 1:
            dp[y][x] = price[y][x] + min(dp[y-1][0], dp[y-1][2])
        else:
            dp[y][x] = price[y][x] + min(dp[y-1][0], dp[y-1][1])

print(min(dp[N-1]))