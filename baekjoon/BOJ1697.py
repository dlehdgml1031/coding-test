from collections import deque

MAX = int(100_000)

N, K = map(int, input().split())

q = deque()
visited = [False] * (MAX + 1)

q.append((0, N)) # Time, Position
visited[N] = True

while q:
    time, pos = q.popleft()
    
    if pos == K:
        print(time)
        break
    
    for nxt_pos in [pos - 1, pos + 1, pos * 2]:
        if (0 <= nxt_pos <= MAX) and (not visited[nxt_pos]):
            q.append((time + 1, nxt_pos))
            visited[nxt_pos] = True