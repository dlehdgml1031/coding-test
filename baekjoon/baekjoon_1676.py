# 첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)
n = int(input())
fac, count, s = 1, 0, []

for i in range(n, 0, -1):
    fac = fac * i

for i in reversed(str(fac)):
    if i != '0':
        break
    elif i == '0':
        if len(i) == 0:
            count += 1
            s.append(i)
        else:
            if i[-1] == '0':
                count += 1
                s.append(i)
            else:
                count += 1
                break

print(count)