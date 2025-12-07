def combination(index, level, R, N):
    # Base Case
    if level == R:
        print(*choose)
        return
    
    # Recursive Case
    for i in range(index, N):
        choose.append(lst[i])
        combination(i + 1, level + 1, R, N)
        choose.pop()

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    
    r = 6
    n = arr[0]
    lst = arr[1:]
    choose = []
    
    combination(0, 0, r, n)
    print()