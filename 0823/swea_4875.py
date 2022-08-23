T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    maze = [[1] * (N+2)]  # 움직임 시 인덱싱을 편하게 하기위해 벽을 한칸씩 대준다.
    for i in range(N):
        line = list(map(int, list(input())))
        maze.append([1] + line + [1])
        for j in range(N):
            if line[j] == 2:  # 시작점 찾기
                start = (i+1, j+1)
    maze.append([1] * (N+2))
    dr = [1, 0, -1, 0]  # 움직이기 위한 네 방향
    dc = [0, 1, 0, -1]
    stack = [start]
    visited = []
    ans = 0
    while stack:  # dfs
        current = stack.pop()
        if current in visited:
            continue
        visited.append(current)
        next_step = []  # 다음에 갈 곳들
        for d in range(4):  # 주변 네 방향을 다음 발걸음으로 추가
            next_step.append((current[0]+dr[d], current[1]+dc[d]))
        for destination in next_step:  # 한칸 움직일 수 있는곳을 보고
            # 갈 수 있는 길이고, 아직 가지 않은 길이라면
            if maze[destination[0]][destination[1]] != 1 and destination not in visited:
                if maze[destination[0]][destination[1]] == 3:  # 일단 도착점인지 확인
                    ans = 1  # 찾으면 끝
                    break
                stack.append(destination)  # 다음에 갈 곳으로 추가
    print(f'#{test_case} {ans}')
