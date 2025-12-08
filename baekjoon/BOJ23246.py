from collections import defaultdict

n = int(input())
hs = defaultdict(list)

for _ in range(n):
    arr = list(map(int, input().split()))
    hs[arr[0]] = arr[1:]

hs = sorted(
    hs.items(),        
    key = lambda x: (
        x[1][0] * x[1][1] * x[1][2],
        x[1][0] + x[1][1] + x[1][2],
        x[0] 
    )
)

# JOIN 사용
result = [str(hs[i][0]) for i in range(min(3, len(hs)))]
print(' '.join(result))