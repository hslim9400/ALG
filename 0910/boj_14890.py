N, L = map(int, input().split())
board = []
for i in range(N):
    line = list(map(int, input().split()))
    board.append(line)

trans_board = list(zip(*board))
ans = 0
for i in range(N):
    flag = False
    bridge = [0] * N
    for j in range(1, N):
        if board[i][j] == board[i][j-1]:
            continue
        if board[i][j] == board[i][j-1] - 1:
            if j + L - 1 >= N:
                break
            for k in range(L):
                if board[i][j+k] != board[i][j] or bridge[j+k]:
                    flag = True
                    break
            else:
                for k in range(L):
                    bridge[j+k] = 1
        elif board[i][j] == board[i][j-1] + 1:
            if j - L < 0:
                break
            for k in range(L):
                if board[i][j-1-k] != board[i][j-1] or bridge[j-1-k]:
                    flag = True
                    break
            else:
                for k in range(L):
                    bridge[j-1-k] = 1
        else:
            break
        if flag:
            break
    else:
        ans += 1
for i in range(N):
    flag = False
    bridge = [0] * N
    for j in range(1, N):
        if trans_board[i][j] == trans_board[i][j-1]:
            continue
        if trans_board[i][j] == trans_board[i][j-1] - 1:
            if j + L - 1 >= N:
                break
            for k in range(L):
                if trans_board[i][j+k] != trans_board[i][j] or bridge[j+k]:
                    flag = True
                    break
            else:
                for k in range(L):
                    bridge[j+k] = 1
        elif trans_board[i][j] == trans_board[i][j-1] + 1:
            if j - L < 0:
                break
            for k in range(L):
                if trans_board[i][j-1-k] != trans_board[i][j-1] or bridge[j-1-k]:
                    flag = True
                    break
            else:
                for k in range(L):
                    bridge[j-1-k] = 1
        else:
            break
        if flag:
            break
    else:
        ans += 1
print(ans)
