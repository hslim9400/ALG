def simulate():
    global board, cells
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    reproduce = {}
    for cell in board.keys():
        board[cell][1] += 1
        if board[cell][0] == board[cell][1]:
            cells -= 1
        if board[cell][1] == 1:
            for d in range(4):
                if (cell[0]+dr[d], cell[1]+dc[d]) not in board.keys():
                    if (cell[0]+dr[d], cell[1]+dc[d]) not in reproduce.keys():
                        reproduce[(cell[0]+dr[d], cell[1]+dc[d])] = board[cell][0]
                    else:
                        reproduce[(cell[0]+dr[d], cell[1]+dc[d])] = max(reproduce[(cell[0]+dr[d], cell[1]+dc[d])], board[cell][0])
    for cell in reproduce:
        board[cell] = [reproduce[cell], -reproduce[cell]]
        cells += 1


T = int(input())
for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    board = {}
    cells = 0
    for i in range(N):
        line = list(map(int, input().split()))
        for j in range(M):
            if line[j]:
                board[(i, j)] = [line[j], -line[j]]
                cells += 1

    for t in range(K):
        simulate()
    print(f'#{test_case} {cells}')