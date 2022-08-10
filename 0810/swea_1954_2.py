T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    board = []
    for _ in range(N):
        board = board + [[0]*N]

    dx, dy = [0, 1, 0, -1] * N, [1, 0, -1, 0] * N
    x, y, d, num = 0, 0, 0, 1

    while num != (N**2)+1:
        board[x][y] = num
        if (0 <= x+dx[d] < N) and (0 <= y+dy[d] < N) and (board[x+dx[d]][y+dy[d]] == 0):
            pass
        else:
            d = d + 1
        x = x + dx[d]
        y = y + dy[d]
        num = num + 1

    print(f'#{test_case}')
    for i in range(N):
        print(' '.join(list(map(str, board[i]))))