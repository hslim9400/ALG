def next_row(row):
    global counts, board
    if row == N:  # 마지막 칸 아래에 도달하면 1개 카운트
        counts += 1
        return

    for i in range(N):  # 한 칸을 찍고
        if i in board[row]:  # 찍은 칸에 놓을 수 있는지 확인
            restore = []
            for j in range(N-row):  # 퀸을 놓고 퀸의 공격로를 보드에서 지운다.
                restore.append([])
                if i in board[row+j]:
                    board[row+j].remove(i)
                    restore[-1].append(i)
                if i+j in board[row+j]:
                    board[row+j].remove(i+j)
                    restore[-1].append(i+j)
                if i-j in board[row+j]:
                    board[row+j].remove(i-j)
                    restore[-1].append(i-j)

            next_row(row+1)  # 다음칸으로 내려간다.

            for j in range(N-row):
                for k in range(len(restore[j])):
                    board[row+j].append(restore[j][k])


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    board = [[i for i in range(N)] for _ in range(N)]
    counts = 0
    next_row(0)
    print(f'#{test_case} {counts}')