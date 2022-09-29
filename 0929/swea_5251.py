def dijkstra():
    dist = [10*E] * (N+1)
    dist[0] = 0
    visited = [0] * (N+1)

    for _ in range(N):
        min_idx = -1
        min_value = 10 * E

        for i in range(N+1):
            if not visited[i] and dist[i] < min_value:
                min_idx = i
                min_value = dist[i]

        visited[min_idx] = 1

        for i in range(N+1):
            if not visited[i] and dist[i] > adj[min_idx][i] + dist[min_idx]:
                dist[i] = adj[min_idx][i] + dist[min_idx]

    return dist[N]


T = int(input())
for test_case in range(1, T+1):

    N, E = map(int ,input().split())
    adj = [[10*E]*(N+1) for _ in range(N+1)]
    for _ in range(E):
        start, end, weight = map(int, input().split())
        adj[start][end] = weight

    print(f'#{test_case} {dijkstra()}')