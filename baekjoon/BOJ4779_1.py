# Solve 1: Bottom up case
# f(n): 입력이 n일 때의 정답으로 가정
# f(n): f(n-1) + 공백 3^(n-1) + f(n-1)

ans = ['' for _ in range(13)]
ans[0] = '-'

for i in range(1, 13):
    ans[i] = ans[i-1] + (' ' * (3 ** (i - 1))) + ans[i-1]

while True:
    try:
        N = int(input())
        print(ans[N])
    except:
        break