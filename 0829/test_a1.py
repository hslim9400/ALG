def connect_power(r, c, powered, used):
    global max_powered, min_used
    if r == N:
        if powered >= max_powered:
            if min_used > used:
                min_used = used
            max_powered = powered
        return

    if c == N:
        connect_power(r+1, 0, powered, used)
        return

    if board[r][c] == 0 or board[r][c] == -1:
        connect_power(r, c+1, powered, used)
        return

    if r == 0 or r == N-1 or c == 0 or c == N-1:
        powered += 1
        connect_power(r, c+1, powered, used)
        return

    flag = True
    for i in range(0, r):  # 윗 방향
        if board[i][c] != 0:
            break
    else:
        powered += 1
        used += r
        for i in range(0, r):
            board[i][c] = -1
        connect_power(r, c+1, powered, used)
        flag = False
        powered -= 1
        used -= r
        for i in range(0, r):
            board[i][c] = 0

    for i in range(r+1, N):  # 아랫 방향
        if board[i][c] != 0:
            break
    else:
        powered += 1
        used += N-r-1
        for i in range(r+1, N):
            board[i][c] = -1
        connect_power(r, c + 1, powered, used)
        flag = False
        powered -= 1
        used -= N-r-1
        for i in range(r+1, N):
            board[i][c] = 0

    for j in range(0, c):  # 왼쪽 방향
        if board[r][j] != 0:
            break
    else:
        powered += 1
        used += c
        for j in range(0, c):
            board[r][j] = -1
        connect_power(r, c+1, powered, used)
        flag = False
        powered -= 1
        used -= c
        for j in range(0, c):
            board[r][j] = 0

    for j in range(c+1, N):  # 오른쪽 방향
        if board[r][j] != 0:
            break
    else:
        powered += 1
        used += N-c-1
        for j in range(c+1, N):
            board[r][j] = -1
        connect_power(r, c + 1, powered, used)
        flag = False
        powered -= 1
        used -= N-c-1
        for j in range(c+1, N):
            board[r][j] = 0
    if flag:
        connect_power(r, c+1, powered, used)


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    board = []
    for _ in range(N):
        line = list(map(int, input().split()))
        board.append(line)

    max_powered = 0
    min_used = N*N
    connect_power(0, 0, 0, 0)

    print(f'#{test_case} {min_used}')

