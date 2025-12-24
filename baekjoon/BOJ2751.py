import sys

input = sys.stdin.readline

n = int(input())
l = [int(input()) for _ in range(n)]

l.sort()
print(*l, sep = '\n')