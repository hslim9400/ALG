def dfs(start, group):
    visited = [0] * (N+1)
    stack = [start]
    counts = 0
    while stack:
        current = stack.pop()
        if visited[current]:
            continue
        visited[current] = 1
        counts += 1
        for destination in group:
            if adj[current][destination] and not visited[destination]:
                stack.append(destination)
    return counts


N = int(input())

cities = [0] + list(map(int, input().split()))
adj = [[0]*(N+1) for _ in range(N+1)]
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(1, len(line)):
        adj[i+1][line[j]] = 1
        adj[line[j]][i+1] = 1

min_diff = 100 * N
for i in range((1<<N)//2):
    group_a = set()
    group_b = set()
    p = list(range(N + 1))
    r = [0] * (N + 1)
    a_start = 0
    b_start = 0
    for j in range(N):
        if i & (1<<j):
            group_a.add(j+1)
            a_start = j+1
        else:
            group_b.add(j+1)
            b_start = j+1
    if not a_start or not b_start:
        continue
    if len(group_a) != dfs(a_start, group_a) or len(group_b) != dfs(b_start, group_b):
        continue
    a_population, b_population = 0, 0
    for area in group_a:
        a_population += cities[area]
    for area in group_b:
        b_population += cities[area]
    diff = abs(a_population - b_population)
    if diff < min_diff:
        min_diff = diff
if min_diff == N*100:
    min_diff = -1
print(min_diff)