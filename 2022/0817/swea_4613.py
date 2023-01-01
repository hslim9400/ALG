T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    board = []
    for _ in range(N):
        board.append(input())
    min_count = N * M
    for w_row in range(1, N-1):
        for b_row in range(1, N-w_row):
            r_row = N - w_row - b_row
            count_change = 0
            for i in range(w_row):
                count_change += M - board[i].count('W')
            for i in range(b_row):
                count_change += M - board[w_row+i].count('B')
            for i in range(r_row):
                count_change += M - board[N-1-i].count('R')
            if count_change < min_count:
                min_count = count_change
    print(f'#{test_case} {min_count}')