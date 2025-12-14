N = int(input())
arr = set([input() for _ in range(N)])
arr = sorted(arr, key = lambda x: (len(x), x))

print(*arr, sep = "\n")