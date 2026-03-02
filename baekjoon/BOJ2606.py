from collections import deque

def dfs(node):
    global adj_list, visited, res
    
    if visited[node]:
        return
    visited[node] = True
    res += 1
    
    for adj_node in adj_list[node]:
        dfs(adj_node)

def bfs(node):
    global adj_list, visited, res
    
    q = deque()
    q.append(node)
    visited[node] = True
    
    while q:
        node = q.popleft()
        res += 1
        
        for adj_node in adj_list[node]:
            if visited[adj_node]:
                continue
            q.append(adj_node)
            visited[adj_node] = True

N = int(input())
M = int(input())

adj_list = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
res = 0

for _ in range(M):
    a, b = map(int,input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)
    
bfs(1)
print(res - 1)