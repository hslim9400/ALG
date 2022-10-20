def rotate(start_r, start_c):
    global board
    new_part = [[0]*stride for _ in range(stride)]
    target_part = [board[i][start_c:start_c+stride] for i in range(start_r, start_r+stride)]

    for r in range(stride):
        for c in range(stride):
            new_part[r][c] = target_part[stride-1-c][r]
    for r in range(stride):
        for c in range(stride):
            board[start_r+r][start_c+c] = new_part[r][c]


def dfs(start_r, start_c):
    global visited
    targets = []
    stack = [(start_r, start_c)]
    while stack:
        current = stack.pop()
        r, c = current[0], current[1]
        if visited[r][c]:
            continue
        visited[r][c] = 1
        targets.append(current)
        for d in range(4):
            nr, nc = r+dr[d], c+dc[d]
            if 0 <= nr < n and 0 <= nc < n:
                if board[nr][nc] and not visited[nr][nc]:
                    stack.append((nr, nc))

    return targets


def melt(board):
    global total
    new_board = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if board[r][c]:
                counts = 0
                for d in range(4):
                    if 0 <= r + dr[d] < n and 0 <= c + dc[d] < n:
                        if board[r + dr[d]][c + dc[d]]:
                            counts += 1
                if counts < 3:
                    new_board[r][c] = board[r][c] - 1
                    total -= 1
                else:
                    new_board[r][c] = board[r][c]
    board = new_board
    return board


N, Q = map(int, input().split())
n = 2**N
board = []
total = 0
for _ in range(n):
    line = list(map(int, input().split()))
    board.append(line)
    total += sum(line)

spells = list(map(int, input().split()))
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
for l in spells:
    stride = 2**l
    for i in range(n//stride):
        for j in range(n//stride):
            rotate(stride*i, stride*j)

    board = melt(board)

visited = [[0] * n for _ in range(n)]
chunk = 0
for i in range(n):
    for j in range(n):
        if board[i][j] and not visited[i][j]:
            target = dfs(i, j)
            if len(target) > chunk:
                chunk = len(target)

print(total)
print(chunk)