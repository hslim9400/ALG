T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    board = []
    for i in range(N):
        line = list(map(int, list(input())))
        board.append(line)
        for j in range(N):
            if line[j] == 2:
                start = (i, j, 0)  # 좌표와 거리를 함께 저장

    queue = [start]
    visited = []
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    ans = 0
    while queue:  # bfs
        current = queue.pop(0)
        if current in visited:
            continue
        visited.append((current[0], current[1]))  # 방문 배열엔 좌표만 저장
        next_step = []
        for d in range(4):
            if 0 <= current[0] + dr[d] < N and 0 <= current[1] + dc[d] < N:  # 보드 안의 네 방향을 둘러보고
                next_step.append((current[0] + dr[d], current[1] + dc[d]))  # 가볼 곳을 추가
        for destination in next_step:  # 가보기로 한 곳에서
            # 벽이거나, 이미 가본 곳이라면 가지 않을 것
            if board[destination[0]][destination[1]] != 1 and (destination[0], destination[1]) not in visited:
                if board[destination[0]][destination[1]] == 3:  # 목적지에 도착
                    ans = current[2]  # 지나간 칸의 개수를 세므로 1을 추가하지 않음
                    queue.clear()  # while문 종료시킴
                    break
                else:
                    # 목적지가 아니라면 갈 곳 목록에 추가
                    queue.append((destination[0], destination[1], current[2]+1))

    print(f'#{test_case} {ans}')

