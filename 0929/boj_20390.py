def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    p[find_set(y)] = find_set(x)


N = int(input())
A, B, C, D = map(int, input().split())
costs = list(map(int, input().split()))
edges = []
p = list(range(N))
for i in range(N-1):
    for j in range(i+1, N):
        dist = ((costs[i]*A + costs[j]*B) % C) ^ D
        edges.append([dist, i, j])

edges.sort()
total_costs = 0
selected = 0
for dist, x, y in edges:
    if find_set(x) != find_set(y):
        union(x, y)
        total_costs += dist
        selected += 1
    if selected == N-1:
        break

print(total_costs)

