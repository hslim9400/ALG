def floyd_warshall():
    dists = [[INF]*(n+1) for _ in range(n+1)]  # 무한대로 초기 설정

    for i in range(1, n+1):
        for j in range(1, n+1):
            dists[i][j] = adj[i][j]  # 연결되어 있는 노드들을 이어준다.
            if i == j:  # 나 -> 나는 거리가 0
                dists[i][j] = 0

    for k in range(1, n+1):  # i에서 j까지 갈 때 지나갈 수 있는 노드
        for i in range(1, n+1):
            for j in range(1, n+1):
                # 해당 노드를 경유하는 것이 더 짧은 거리가 된다면 갱신
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