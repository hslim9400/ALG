from collections import deque

N = int(input())
populations = [0] + list(map(int, input().split()))
adj = [[] for _ in range(N+1)]
for i in range(N-1):
    start, end = map(int, input().split())
    adj[start].append(end)
    adj[end].append(start)

parent = [0] * (N+1)
children = [set() for _ in range(N+1)]
stack = [1]
visited = set()
while stack:
    current = stack.pop()
    if current in visited:
        continue
    visited.add(current)
    for destination in adj[current]:
        if destination not in visited:
            stack.append(destination)
            parent[destination] = current
            children[current].add(destination)

result = [[0, 0, 0] for _ in range(N+1)]
# 우수마을
queue = deque([])
for i in range(1, N+1):
    if not children[i]:
        queue.append(i)

while queue:
    current = queue.popleft()
    if children[current] or current == 1:
        continue
    result[current][0] += populations[current]
    target = parent[current]
    result[target][0] += max(result[current][1], result[current][2])
    result[target][1] += result[current][0]
    result[target][2] += max(result[current][0], result[current][2])
    children[target].discard(current)
    if not children[target]:
        queue.append(target)
result[1][0] += populations[1]
print(max(result[1]))
