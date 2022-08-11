T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    board = [[0]*10 for _ in range(10)]

    for _ in range(N):
        r1, c1, r2, c2, color = list(map(int, input().split()))
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                if board[r][c] != color:
                    board[r][c] = board[r][c] + color

    ans = 0
    for i in range(10):
        for j in range(10):
            if board[i][j] > 2:
                ans = ans + 1

    print(f'#{test_case} {ans}')
