def color_next(blanks, n):
    global ans
    if n == len(blanks):
        ans = 'possible'
        return
    board[blanks[n][0]][blanks[n][1]] = '#'
    for d in range(4):
        if 0 <= blanks[n][0] + dr[d] < N and 0 <= blanks[n][1] + dc[d] < M:
            if board[blanks[n][0] + dr[d]][blanks[n][1] + dc[d]] == '#':
                break
    else:
        color_next(blanks, n+1)
    board[blanks[n][0]][blanks[n][1]] = '.'
    for d in range(4):
        if 0 <= blanks[n][0] + dr[d] < N and 0 <= blanks[n][1] + dc[d] < M:
            if board[blanks[n][0] + dr[d]][blanks[n][1] + dc[d]] == '.':
                break
    else:
        color_next(blanks, n + 1)
    board[blanks[n][0]][blanks[n][1]] = '?'


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    board = []
    blanks = []
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    flag = False
    for i in range(N):
        line = list(input())
        board.append(line)
        for j in range(M):
            if line[j] == '?':
                blanks.append((i, j))
    for i in range(N):
        for j in range(M):
            for d in range(4):
                if 0 <= i + dr[d] < N and 0 <= j + dc[d] < M:
                    if board[i][j] != '?' and board[i][j] == board[i+dr[d]][j+dc[d]]:
                        flag = True

    ans = 'impossible'
    if flag:
        print(f'#{test_case} {ans}')
        continue
    color_next(blanks, 0)
    print(f'#{test_case} {ans}')




