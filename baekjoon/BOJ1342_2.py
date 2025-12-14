def func(lev):
    global S, chars, cnt, choose, ans
    
    # base case
    if lev == len(S):
        ans += 1
        return
    
    # recursive case
    for c in chars:
        if cnt[c] == 0:
            continue
        
        # 답이 될 수 없는 경우 제외
        if (not choose) or (choose[-1] != c):
            cnt[c] -= 1
            choose.append(c)
            func(lev + 1)
            cnt[c] += 1
            choose.pop()
            
S = input()
chars = set()
cnt = dict()

for c in S:
    chars.add(c)
    if c not in cnt:
        cnt[c] = 0
    cnt[c] += 1
    
choose = []
ans = 0

func(0)

print(ans)