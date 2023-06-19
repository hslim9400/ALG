T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(input()))

    dr = [0, 1, 1, 1]
    dc = [1, 0, -1, 1]
    flag_1 = False
    flag_2 = False
    ans = 'NO'
    for i in range(N):
        if flag_1:
            break
        for j in range(N):
            if flag_2:
                break
            if board[i][j] == 'o':
                if 2 <= i < N-2 and 2 <= j < N-2:
                    for d in range(4):
                        for k in range(1, 3):
                            if board[i + k*dr[d]][j + k*dc[d]] == '.' or board[i - k*dr[d]][j - k*dc[d]] == '.':
                                break
                        else:
                            ans = 'YES'
                            flag_1 = True
                            flag_2 = True
                            break
                elif 2 <= i < N-2:
                    d = 1
                    for k in range(1, 3):
                        if board[i + k*dr[d]][j + k*dc[d]] == '.' or board[i - k*dr[d]][j - k*dc[d]] == '.':
                            break
                    else:
                        ans = 'YES'
                        flag_1 = True
                        flag_2 = True
                        break
                elif 2 <= j < N-2:
                    d = 0
                    for k in range(1, 3):
                        if board[i + k*dr[d]][j + k*dc[d]] == '.' or board[i - k*dr[d]][j - k*dc[d]] == '.':
                            break
                    else:
                        ans = 'YES'
                        flag_1 = True
                        flag_2 = True
                        break

    print(f'#{test_case} {ans}')
