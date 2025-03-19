while True:
    a = list(map(int, input().split()))
    
    if 0 in a:
        break
    
    max_value = max(a)
    a.remove(max_value)
    
    if (max_value ** 2) == ((a[0] ** 2) + (a[1] ** 2)):
        print('right')
    else:
        print('wrong')