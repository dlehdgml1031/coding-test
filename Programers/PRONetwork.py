def solution(n, computers):
    visited = [False] * n
    
    def dfs(node):
        visited[node] = True
        for nxt in range(n):
            if computers[node][nxt] == 1 and visited[nxt] != True:
                dfs(nxt)
                
    answer = 0
    for i in range(n):
        if visited[i] != True:
            dfs(i)
            answer += 1
    
    return answer