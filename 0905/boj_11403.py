from collections import deque


N = int(input())
adj = []
for i in range(N):
    line = list(map(int, input().split()))
    adj.append(line)
can_go = [[0]*N for _ in range(N)]
for i in range(N):
    queue = deque()
    visited = [0] * N
    for j in range(N):
        if adj[i][j]:
            queue.append(j)
    while queue:
        current = queue.popleft()
        if visited[current]:
            continue
        visited[current] = 1
        can_go[i][current] = 1
        for destination in range(N):
            if adj[current][destination] and not visited[destination]:
                queue.append(destination)
for i in range(N):
    print(*can_go[i])

