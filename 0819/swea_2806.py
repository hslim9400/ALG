def next_row(board, row):
    global counts
    if row == N:  # 마지막 칸 아래에 도달하면 1개 카운트
        counts += 1
        return

    for i in range(N):  # 한 칸을 찍고
        clone = board[:]  # 보드를 조작하기 위해 복사
        if (row, i) in clone:  # 찍은 칸에 놓을 수 있는지 확인
            for j in range(N-row):  # 퀸을 놓고 퀸의 공격로를 보드에서 지운다.
                if (row+j, i) in clone:
                    clone.remove((row+j, i))
                if (row+j, i+j) in clone:
                    clone.remove((row+j, i+j))
                if (row+j, i-j) in clone:
                    clone.remove((row+j, i-j))
            next_row(clone, row+1)  # 다음칸으로 내려간다.

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    board = []
    for i in range(N):
        for j in range(N):
            board.append((i, j))  # 보드를 복사하기 위해 2차원이 아닌 1차원 배열로 만든다. 좌표들을 저장
    clone = board[:]
    counts = 0
    next_row(clone, 0)
    print(f'#{test_case} {counts}')