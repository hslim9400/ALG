# 문제가 상어랑 뭔 상관인지 모르겠음
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def find_group():  # 제거할 그룹을 찾는 함수
    # 없다면 빈 리스트를 반환할 것.
    visited = [[0]*N for _ in range(N)]
    target = []  # 반환할 리스트
    max_counts = 0
    for i in range(N):
        for j in range(N):
            # 모든 좌표에 대해 dfs를 수행하여 그룹을 묶어준다.
            # 0인 친구들은 다른 숫자에 대해서도 방문해야 하기 때문에 visited를 0으로 바꿔준다.
            stack = []
            if visited[i][j] or board[i][j] < 1:
                continue
            target_num = board[i][j]  # 그룹의 숫자를 정하고
            stack.append((i, j))
            current_group = []  # 개수를 셀 현재 그룹
            rainbows = []  # 나중에 visited를 다시 0으로 바꿔줄 무지개블록
            counts = 0
            while stack:  # dfs 수행, 해당 숫자와 0을 찾아 넣는다.
                current = stack.pop()
                r, c = current[0], current[1]
                if visited[r][c]:
                    continue
                visited[r][c] = 1
                if not board[r][c]:
                    counts += 1
                    rainbows.append(current)
                current_group.append(current)
                for d in range(4):
                    if 0 <= r+dr[d] < N and 0 <= c+dc[d] < N:
                        if not visited[r+dr[d]][c+dc[d]] and \
                                (board[r+dr[d]][c+dc[d]] == 0 or board[r+dr[d]][c+dc[d]] == target_num):
                            stack.append((r+dr[d], c+dc[d]))
            if len(current_group) > 1:  # 그룹 갱신 조건, 1개짜리는 그룹이 안됨
                if len(current_group) > len(target):  # 가장 큰 그룹일 경우 갱신
                    target = current_group
                    max_counts = counts
                if len(current_group) == len(target):  # 크기는 같고 무지개블럭이 많을경우 갱신
                    if counts > max_counts:
                        target = current_group
                        max_counts = counts
                    if counts == max_counts:
                        target = current_group  # 무지개블럭도 같다면 r,c가 큰 녀석으로 갱신
            for rainbow in rainbows:  # 무지개블럭들의 visited를 초기화
                visited[rainbow[0]][rainbow[1]] = 0

    return target


def counter_clock():  # 반시계방향 회전
    new_board = [[-2] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            new_board[N-1-j][i] = board[i][j]
    return new_board


def gravity():  # 아래로 내리기
    new_board = [[-2]*N for _ in range(N)]

    for j in range(N):
        bottom = N - 1
        for i in range(N-1, -1, -1):
            if board[i][j] == -1:
                new_board[i][j] = -1
                bottom = i - 1  # 검은 블럭은 움직이지 않기 때문에 포인터를 검은 블럭 위로 올려준다.
            elif board[i][j] >= 0:  # 중력으로 내려가는 애를 만나면 현재 포인터에
                # 해당 블럭을 적고 포인터를 올려줌
                new_board[bottom][j] = board[i][j]
                bottom -= 1
    return new_board


N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

ans = 0
while True:  # 발견되는 그룹이 없을 때까지 수행
    targets = find_group()  # 그룹 찾기
    if not targets:  # 그룹이 없으면 종료
        break

    ans += len(targets) * len(targets)  # 그룹이 있다면 조건에 따라 점수 추가
    for target in targets:  # 그룹에 포함된 블럭들 제거하기
        r, c = target[0], target[1]
        board[r][c] = -2  # 나는 -2를 빈 공간으로 하기로 함 
    board = gravity()  # 내리고 돌리고 내리고
    board = counter_clock()
    board = gravity()
print(ans)
