n = int(input())
arr = [i for i in range(1, n + 1)]
check = [False] * len(arr)
choose = []

def permutation(level):
    if level == n:
        print(*choose)
        return
    
    for i in range(0, len(arr)):
        if check[i] == True:
            continue
        choose.append(arr[i])
        check[i] = True
        
        permutation(level + 1)
        
        check[i] = False
        choose.pop()
        
permutation(0)