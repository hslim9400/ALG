for tc in range(10):
    test_case = int(input())
    maze = []
    for i in range(100):
        line = list(map(int, list(input())))  # 한 줄을 받는다.
        maze.append(line)
        for j in range(100):
            if line[j] == 2:  # 그 줄에 2가 있다면 시작점
                start = [i, j]
            if line[j] == 3:  # 3이 있다면 끝점
                end = [i, j]

    dr = [1, 0, -1, 0]  # 방향탐색용 좌표
    dc = [0, 1, 0, -1]
    stack = []
    stack.append(start)  # 갈 수 있는지만 확인하기 떄문에 거리는 저장하지 않음
    visited = []

    while stack:  # dfs
        current = stack.pop()
        if current not in visited:
            visited.append(current)
        next_steps = []
        for d in range(4):
            if maze[current[0] + dr[d]][current[1] + dc[d]] != 1:  # 네 방향을 보고 벽이 아니라면
                next_steps.append([current[0]+dr[d], current[1]+dc[d]])  # 둘러 볼 것.

        for next_step in next_steps:
            if next_step not in visited:  # 아직 방문하지 않았다면
                stack.append(next_step)  # 갈 곳에 추가

    ans = 0
    if end in visited:
        ans = 1
    print(f'#{test_case} {ans}')
