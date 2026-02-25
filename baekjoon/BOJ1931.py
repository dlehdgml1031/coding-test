import sys
input = sys.stdin.readline

N = int(input())
time_table = [list(map(int, input().split())) for _ in range (N)]
time_table = sorted(time_table, key = lambda x: (x[1], x[0]))

ans = 0
end = 0
for s, e in time_table:
    if s >= end:
        ans += 1
        end = e
        
print(ans)