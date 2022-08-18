T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0]*(V+1) for _ in range(V+1)]  # 인접행렬 생성
    for _ in range(E):
        edge = list(map(int, input().split()))
        start = edge[0]
        end = edge[1]
        adj[start][end] = 1  # 인접행렬 바꾸기
    s, g = map(int, input().split())  # 시작점과 끝점
    stack = [s]  # 시작점에서 시작
    visited = []
    while stack:  # dfs
        current = stack.pop()
        if current in visited:
            continue
        visited.append(current)
        for destination in range(V+1):
            if adj[current][destination] and destination not in visited:
                stack.append(destination)

    if g in visited:  # 밟은 곳에 g가 있다면 갈 수 있다. dfs에 넣고 브레이크 걸어도 가능
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')