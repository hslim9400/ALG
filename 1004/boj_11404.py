def floyd_warshall():
    dists = [[INF]*(n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            dists[i][j] = adj[i][j]
            if i == j:
                dists[i][j] = 0


    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if dists[i][j] > dists[i][k] + dists[k][j]:
                    dists[i][j] = dists[i][k] + dists[k][j]

    return dists


n = int(input())
e = int(input())
INF = float('inf')
adj = [[INF]*(n+1) for _ in range(n+1)]
for i in range(e):
    start, end, weight = map(int, input().split())
    adj[start][end] = min(adj[start][end], weight)

dists = floyd_warshall()
for i in range(1, n+1):
    for j in range(1, n+1):
        if dists[i][j] == INF:
            dists[i][j] = 0
    print(*dists[i][1:])