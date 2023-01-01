from collections import deque
# 오늘따라 덱이 쓰고싶다

N = int(input())
adj = []  # 인접행렬이 입력으로 주어짐
for i in range(N):
    line = list(map(int, input().split()))
    adj.append(line)
can_go = [[0]*N for _ in range(N)]  # 이 캔고 행렬을 조작하여 답으로 출력할 예정
for i in range(N):  # 모든 원소에 대해
    queue = deque()
    visited = [0] * N
    for j in range(N):
        if adj[i][j]:  # 내가 한번에 도달할 수 있는 애들을 모아서
            queue.append(j)
    while queue: # bfs로 도달할 수 있는 모든 정점을 모은다.
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

