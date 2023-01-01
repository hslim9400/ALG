import heapq


def dijkstra():
    dists = [10001*(N+1)] * (N+1)
    dists[2] = 0
    visited = set()
    heap = [(0,2)]
    while heap:
        dist, current = heapq.heappop(heap)
        if current in visited:
            continue
        visited.add(current)
        dists[current] = dist
        for destination in adj[current]:
            if destination[0] not in visited and dists[destination[0]] > destination[1] + dists[current]:
                heapq.heappush(heap, (destination[1] + dists[current], destination[0]))
    return dists


def find_path(current):  # 재귀 dp
    global dp

    if dp[current]:
        return dp[current]
    else:
        for destination in adj[current]:
            if dists[destination[0]] < dists[current]:
                dp[current] += find_path(destination[0])
        return dp[current]


N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))
dists = dijkstra()  # 2기준으로 다익스트라
dp = [0] * (N+1)
dp[2] = 1

ans = find_path(1)
print(ans)
