def f_w():
    dists = [[inf]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            dists[i][j] = adj[i][j]
            if i == j:
                dists[i][j] = 0

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dists[i][j] = min(dists[i][j], dists[i][k] + dists[k][j])
    return dists


n, m, r = map(int, input().split())
areas = [0] + list(map(int, input().split()))
inf = float('inf')
adj = [[inf] * (n+1) for _ in range(n+1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    adj[a][b] = adj[b][a] = l
dists = f_w()
max_items = 0
for i in range(1, n+1):
    items = 0
    for j in range(1, n+1):
        if dists[i][j] <= m:
            items += areas[j]
    max_items = max(max_items, items)

print(max_items)
