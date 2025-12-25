N = int(input())

arr1 = [5 * i for i in range(1000 + 1)]
arr2 = [3 * i for i in range(1800 + 1)]

min_cnt = 1e10
flag = False

for i in range(len(arr1)):
    for j in range(len(arr2)):
        if arr1[i] + arr2[j] == N:
            flag = True
            if (i + j) < min_cnt:
                min_cnt = i + j

if flag:
    print(min_cnt)
else:
    print(-1)