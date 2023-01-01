dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def change_board(p, q):
    global visited, board, marked
    stack = [(p, q)]
    for i in range(1, 7):
        if not marked[i]:
            marker = i
            marked[i] = 1
            break

    while stack:
        r, c = stack.pop()
        if visited[r][c]:
            continue
        board[r][c] = marker
        visited[r][c] = 1
        for d in range(4):
            if 0 <= r+dr[d] < N and 0 <= c+dc[d] < M:
                if board[r+dr[d]][c+dc[d]] and not visited[r+dr[d]][c+dc[d]]:
                    stack.append((r+dr[d], c+dc[d]))


def prim():
    dists = [20] * (targets+1)
    dists[1] = 0
    visited = [0] * (targets+1)

    for _ in range(targets):
        min_idx = -1
        min_value = 20

        for i in range(1, targets+1):
            if not visited[i] and dists[i] < min_value:
                min_idx = i
                min_value = dists[i]
        visited[min_idx] = 1

        for i in range(1, targets+1):
            if not visited[i] and dists[i] > adj[min_idx][i]:
                dists[i] = adj[min_idx][i]
    for i in range(1, targets+1):
        if dists[i] == 20:
            return -1
    return sum(dists[1:])


N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
marked = [0] * 8
visited = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j]:
            if not visited[i][j]:
                change_board(i, j)

trans_board = list(zip(*board))
for i in range(1, 8):
    if not marked[i]:
        targets = i - 1
        break
adj = [[20]*(targets+1) for _ in range(targets+1)]

for i in range(N):
    flag = False
    dist = 0
    for j in range(M):
        if not board[i][j]:
            if flag:
                dist += 1
        else:
            if board[i][j] != flag:
                if adj[flag][board[i][j]] > dist > 1:
                    adj[flag][board[i][j]] = dist
                    adj[board[i][j]][flag] = dist
                dist = 0
                flag = board[i][j]
            else:
                dist = 0
for i in range(M):
    flag = 0
    dist = 0
    for j in range(N):
        if not trans_board[i][j]:
            if flag:
                dist += 1
        else:
            if trans_board[i][j] != flag:
                if adj[flag][trans_board[i][j]] > dist > 1:
                    adj[flag][trans_board[i][j]] = dist
                    adj[trans_board[i][j]][flag] = dist
                dist = 0
                flag = trans_board[i][j]
            else:
                dist = 0

print(prim())
