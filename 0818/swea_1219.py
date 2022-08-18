for test_case in range(1, 11):
    t, E = map(int, input().split())
    V = 100
    adj = [[0]*100 for _ in range(100)]  # 시작이 0, 도착이 99이므로 100*100으로 생성
    edge_list = list(map(int, input().split()))
    for i in range(E):
        start = edge_list[2*i]
        end = edge_list[2*i + 1]
        adj[start][end] = 1  # 인접행렬 조작
    stack = [0]
    visited = []
    flag = False  # 브레이크를 위한 플래그
    while stack:  # dfs
        current = stack.pop()
        if current in visited:
            continue
        visited.append(current)
        for destination in range(100):
            if adj[current][destination] and destination not in visited:
                if destination == 99:  # 도착점을 찾으면 브레이크
                    flag = True
                    print(f'#{test_case} 1')
                stack.append(destination)

    if flag:
        continue

    print(f'#{test_case} 0')