def dfs(start):
    dists = [0] * (N+1)
    visited = [0] * (N+1)
    stack = [(start, 0)]
    end = 0
    end_dist = 0
    while stack:
        current = stack.pop()
        current, dist = current[0], current[1]
        if visited[current]:
            continue
        dists[current] = dist
        visited[current] = 1
        if dist > end_dist:
            end_dist = dist
            end = current
        for destination, add_dist in adj[current]:
            if not visited[destination]:
                stack.append((destination, dist+add_dist))

    return end, end_dist


N = int(input())

adj = [[] for _ in range(N+1)]

for _ in range(N):
    info = list(map(int, input().split()))
    node = info[0]
    for i in range(1, len(info)//2):
        adj[node].append([info[2*i-1], info[2*i]])

start, dist = dfs(1)
end, ans = dfs(start)
print(ans)
