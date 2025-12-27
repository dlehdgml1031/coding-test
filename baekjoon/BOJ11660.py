import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [[0] * (N + 1)]
for _ in range(N):
    arr.append([0] + list(map(int, input().split())))

cord = [list(map(int, input().split())) for _ in range(M)]

psum = [[0] * (N + 1) for _ in range(N + 1)]


for i in range(1, N + 1):
    for j in range(1, N + 1):
        psum[i][j] = arr[i][j] + (psum[i - 1][j] + psum[i][j - 1] - psum[i - 1][j - 1])

for x1, y1, x2, y2 in cord:
    print(
        psum[x2][y2] 
        - (psum[x2][y1 - 1] + psum[x1 - 1][y2] - psum[x1 - 1][y1 - 1])
    )