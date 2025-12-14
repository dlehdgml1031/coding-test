from itertools import permutations

def fact(x):
    if x == 0:
        return 1
    return fact(x - 1) * x

S = input()
ans = 0

for perm in permutations(S):
    flag = True
    
    for i in range(0, len(S) - 1):
        if perm[i] == perm[i + 1]:
            flag = False
            break
    ans += flag

for i in range(ord('a'), ord('z') + 1):
    ans //= fact(S.count(chr(i)))
    
print(ans)