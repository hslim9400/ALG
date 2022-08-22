T = int(input())
for test_case in range(1, T+1):
    N, S, E = map(int, input().split())
    M = int(input())
    A = []
    B = []
    for i in range(M):
        Ai, Bi = map(int, input().split())
        A.append(Ai)
        B.append(Bi)
    adj = [[0]*(N+1) for _ in range(N+1)]
    for k in range(M):
        Na = N // A[k]
        Nb = N // B[k]
        for i in range(1, Na + 1):
            for j in range(1, Nb + 1):
                adj[A[k]*i][B[k]*j] = 1
    dists = [0]
    que = [S]
    visited = []
    ans = -1
    while que:
        current = que.pop(0)
        node_dist = dists.pop(0)
        if current in visited:
            continue
        visited.append(current)
        print(visited)
        for destination in range(1, N+1):
            if adj[current][destination] and destination not in visited:
                if destination == E:
                    ans = node_dist + 1
                    break
                que.append(destination)
                dists.append(node_dist+1)

    print(f'#{test_case} {ans}')
