N, L = map(int, input().split())
board = []
for i in range(N):
    line = list(map(int, input().split()))
    board.append(line)

trans_board = list(zip(*board))  # 세로에 대해서도 조사해야 하므로 전치한다.
ans = 0
for i in range(N):  # 가로의 경우
    flag = False
    bridge = [0] * N
    for j in range(1, N):
        if board[i][j] == board[i][j-1]:  # 앞칸과 높이가 같다면 다음 칸으로 진행
            continue
        if board[i][j] == board[i][j-1] - 1:  # 앞칸보다 낮다면 내 뒤로 다리를 놓을 수 있는지 확인
            if j + L - 1 >= N:
                break
            for k in range(L):
                if board[i][j+k] != board[i][j] or bridge[j+k]:  # 높이차가 발생하거나 이미 다리가 있거나
                    flag = True  # 망했다
                    break
            else:
                for k in range(L):
                    bridge[j+k] = 1
        elif board[i][j] == board[i][j-1] + 1:  # 앞칸보다 높다면 앞 칸의 앞쪽으로 다리를 놓아야 함.
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
        if flag:  # 다리 못놓는거 확인하면 이 줄은 안된다.
            break
    else:  # 어떻게든 지나가게 만들면 카운트
        ans += 1
for i in range(N):  # 전치행렬에 대해 똑같이 다시한다. for-else로 답을 카운트 하므로 동시에 진행하지 않는다.
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
