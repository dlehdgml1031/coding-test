import sys
from collections import deque

input = sys.stdin.readline

def bfs(node):
    global N, M, arr_list, visited
    
    q = deque()
    q.append(node)
    visited[node] = True
    
    while q:
        curr = q.popleft()
        for adj_node in arr_list[curr]:
            if visited[adj_node]:
                continue
            q.append(adj_node)
            visited[adj_node] = True


N, M = map(int, input().split())
arr_list = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    arr_list[a].append(b)
    arr_list[b].append(a)

ans = 0
for n in range(1, N + 1):
    if not visited[n]:
        bfs(n)
        ans += 1

print(ans)