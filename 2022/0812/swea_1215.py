T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())

    board = []
    for _ in range(8):
        board.append(input())

    ans = 0
    rotated = list(zip(*board))
    for i in range(8):
        for j in range(8 - N + 1):
            check_1 = board[i][j:j + N]
            check_2 = rotated[i][j:j + N]
            flags = [1, 1]
            for k in range(N):
                if check_1[k] != check_1[-k - 1]:
                    flags[0] = 0
                if check_2[k] != check_2[-k - 1]:
                    flags[1] = 0
            ans = ans + sum(flags)

    print(f'#{test_case} {ans}')
