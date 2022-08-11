
for test_case in range(1, 11):
    tc = int(input())
    board = []
    for _ in range(100):
        board.append(list(map(int, input().split())))
    for i in range(100):
        if board[99][i] == 2:
            c = i
    r = 99

    while r > 0:
        r = r - 1
        if 0 < c < 100:  # 1부터 99
            if board[r][c - 1] == 1:
                while True:
                    c = c - 1
                    if c == 0:
                        break
                    elif board[r][c - 1] == 0:
                        break
                continue

        if 0 <= c < 99:  # 0부터 98
            if board[r][c + 1] == 1:
                while True:
                    c = c + 1
                    if c == 99:
                        break
                    elif board[r][c + 1] == 0:
                        break

    print(f'#{test_case} {c}')