n = int(input())
stack, ans, flag = [], [], False
start_num = 1

for _ in range(n):
    num = int(input())
    while start_num <= num:
        stack.append(start_num)
        ans.append('+')
        start_num += 1
    
    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    else:
        print('NO')
        flag = True
        break

if not flag:
    for i in ans:
        print(i)