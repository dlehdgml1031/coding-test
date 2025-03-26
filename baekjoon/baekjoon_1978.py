N = int(input())
num_list = [int(x) for x in input().split()]
ans = 0

for i in num_list:
    flag = 1
    
    if i == 1:
        continue
    if i == 2:
        ans += 1
        continue
    
    if (i % 2) == 0:
        flag = 0
        continue
    else:
        for j in range(2, i):
            if i%j == 0:
                flag = 0
                break
    
    if flag:
        ans +=1
    
print(ans)