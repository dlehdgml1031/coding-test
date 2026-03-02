import sys
from collections import deque

input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    dist = [[-1] * m for _ in range(n)]
    
    q = deque()
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                q.append((i, j))
                dist[i][j] = 0
            elif board[i][j] == 0:
                dist[i][j] = 0
                
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    while q:
        y, x = q.popleft()
        
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            
            if 0 <= ny < n and 0 <= nx < m and dist[ny][nx] == -1:
                if board[ny][nx] == 1:
                    dist[ny][nx] = dist[y][x] + 1
                    q.append((ny, nx))
                    
    for row in dist:
        print(*row)

if __name__ == "__main__":
    solve()