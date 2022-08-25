T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0]*(V+1) for _ in range(V+1)]  # 인접행렬을 만든다.
    for _ in range(E):  # 간선에 맞게 인접행렬을 조정
        start, end = map(int, input().split())
        adj[start][end] = 1
        adj[end][start] = 1

    S, G = map(int, input().split())
    queue = [(S, 0)]  # 노드와 거리를 함께 저장
    visited = []
    ans = 0
    while queue:
        current = queue.pop(0)
        if current[0] in visited:  # 방문 목록에는 노드만 저장
            continue
        visited.append(current[0])
        for destination in range(V+1):
            # 인접행렬을 보고 갈 수 있으며 아직 가지 않았다면
            if adj[current[0]][destination] and destination not in visited:
                if destination == G:  # 목적지 도착시
                    ans = current[1] + 1  # 마지막 이동하므로 거리 +1
                    queue.clear()  # while문 종료
                    break
                else:  # 목적지가 아니라면 다음 갈 곳에 추가
                    queue.append((destination, current[1]+1))
    print(f'#{test_case} {ans}')

