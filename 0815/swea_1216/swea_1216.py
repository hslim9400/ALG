import sys
sys.stdin = open("input.txt", "r")
T = 10
for test_case in range(1, T + 1):
    tc = int(input())
    board = []
    for _ in range(100):
        board.append(list(input()))
    trans_board = list(zip(*board))

    max_circular = 100
    flag = False
    for k in range(99, -1, -1):
        if flag:
            break
        for i in range(100-k+1):
            for j in range(100):
                if (board[j][i: i+k] == board[j][i: i+k][::-1]) or\
                        (trans_board[j][i: i+k] == trans_board[j][i: i+k][::-1]):
                    max_circular = k
                    flag = True
                    break

    print(f'#{test_case} {max_circular}')
