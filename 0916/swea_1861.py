T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    max_dist = 0
    start_num = 0
    for i in range(N):
        for j in range(N):
            dist = 1
            current = (i, j)
            while True:
                r = current[0]
                c = current[1]
                for d in range(4):
                    if 0 <= r+dr[d] < N and 0 <= c+dc[d] < N:
                        if board[r+dr[d]][c+dc[d]] == board[r][c] + 1:
                            current = (r+dr[d], c+dc[d])
                            dist += 1
                            break
                else:
                    break
            if dist > max_dist:
                max_dist = dist
                start_num = board[i][j]
            if dist == max_dist:
                if board[i][j] < start_num:
                    start_num = board[i][j]
    print(f'#{test_case} {start_num} {max_dist}')