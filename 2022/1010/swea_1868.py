def dfs(start_r, start_c):
    global visited
    stack = [(start_r, start_c)]
    while stack:
        r, c = stack.pop()
        if visited[r][c]:
            continue
        visited[r][c] = 1
        if board[r][c]:
            continue
        for dr in [0, 1, -1]:
            for dc in [0, 1, -1]:
                if 0 <= r+dr < N and 0 <= c+dc < N:
                    if not visited[r+dr][c+dc] and board[r+dr][c+dc] != -1:
                        stack.append((r+dr, c+dc))


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    board = []
    mines = []
    for i in range(N):
        line = list(input())
        for j in range(N):
            if line[j] == '.':
                line[j] = 0
            else:
                line[j] = -1
                mines.append((i, j))
        board.append(line)

    for mine in mines:
        for dr in [0, 1, -1]:
            for dc in [0, 1, -1]:
                nr = mine[0] + dr
                nc = mine[1] + dc
                if 0 <= nr < N and 0 <= nc < N:
                    if board[nr][nc] != -1:
                        board[nr][nc] += 1

    visited = [[0]*N for _ in range(N)]
    click = 0
    for i in range(N):  # 0부터 눌러주며 dfs를 실행 해 한번에 확장되는 범위를 기록 한 시행에 클릭 한번
        for j in range(N):
            if not board[i][j] and not visited[i][j]:
                dfs(i, j)
                click += 1
    for i in range(N):  # 아직 가지 않은 곳들은 개별적으로 눌러 줘야 함
        for j in range(N):
            if board[i][j] != -1 and not visited[i][j]:
                click += 1

    print(f'#{test_case} {click}')

