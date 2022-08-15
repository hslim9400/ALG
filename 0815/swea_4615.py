def make_move(board, r, c, color):
    global dr, dc, N
    board[r][c] = color
    for i in range(3):
        for j in range(3):
            if i == 0 and j == 0:
                continue
            check = 1
            while True:
                if (0 <= r + check*dr[i] < N) and (0 <= c + check*dc[j] < N):
                    if board[r + check * dr[i]][c + check * dc[j]] == 0:
                        break
                    elif board[r + check*dr[i]][c + check*dc[j]] != color:
                        check += 1
                    else:
                        for ch in range(1, check):
                            board[r + ch*dr[i]][c + ch*dc[j]] = color
                        break
                else:
                    break
    return board


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    board = [[0]*N for _ in range(N)]
    board[N//2][N//2], board[N//2-1][N//2-1] = 2, 2
    board[N//2][N//2-1], board[N//2-1][N//2] = 1, 1
    dr = [0, 1, -1]
    dc = [0, 1, -1]

    for k in range(M):
        c, r, color = map(int, input().split())
        r, c = r - 1, c - 1
        board = make_move(board, r, c, color)

    white = 0
    black = 0
    for i in range(N):
        white += board[i].count(2)
        black += board[i].count(1)
    print(f'#{test_case} {black} {white}')