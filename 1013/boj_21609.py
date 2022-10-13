dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def find_group():
    visited = [[0]*N for _ in range(N)]
    target = []
    max_counts = 0
    for i in range(N):
        for j in range(N):
            stack = []
            if visited[i][j] or board[i][j] < 1:
                continue
            target_num = board[i][j]
            stack.append((i, j))
            current_group = []
            rainbows = []
            counts = 0
            while stack:
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
            if len(current_group) > 1:
                if len(current_group) > len(target):
                    target = current_group
                    max_counts = counts
                if len(current_group) == len(target):
                    if counts > max_counts:
                        target = current_group
                        max_counts = counts
                    if counts == max_counts:
                        target = current_group
            for rainbow in rainbows:
                visited[rainbow[0]][rainbow[1]] = 0

    return target


def counter_clock():
    new_board = [[-2] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            new_board[N-1-j][i] = board[i][j]
    return new_board


def gravity():
    new_board = [[-2]*N for _ in range(N)]

    for j in range(N):
        bottom = N - 1
        for i in range(N-1, -1, -1):
            if board[i][j] == -1:
                new_board[i][j] = -1
                bottom = i - 1
            elif board[i][j] >= 0:
                new_board[bottom][j] = board[i][j]
                bottom -= 1
    return new_board


N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

ans = 0
while True:
    targets = find_group()
    if not targets:
        break

    ans += len(targets) * len(targets)
    for target in targets:
        r, c = target[0], target[1]
        board[r][c] = -2
    board = gravity()
    board = counter_clock()
    board = gravity()
print(ans)
