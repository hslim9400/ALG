from collections import deque

V, E = map(int, input().split())
edges = list(map(int, input().split()))
adj = [[0]*(V+1) for _ in range(V+1)]
for i in range(E):
    start, end = edges[i*2], edges[2*i + 1]
    adj[start][end] = 1

queue = deque([edges[0]])
visited = []

while queue:
    current = queue.popleft()
    if current in visited:
        continue
    visited.append(current)
    for destination in range(V+1):
        if adj[current][destination] and destination not in visited:
            queue.append(destination)

print(visited)