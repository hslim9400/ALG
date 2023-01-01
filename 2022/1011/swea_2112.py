from copy import deepcopy


def change(current_board, depth, count):
    if count > ans:
        return
    if depth == D:
        quality_test(current_board, count)
        return

    A = [0]*W
    B = [1]*W
    change(current_board, depth+1, count)
    current_board[depth] = A
    change(current_board, depth+1, count+1)
    current_board[depth] = B
    change(current_board, depth+1, count+1)
    current_board[depth] = board[depth]


def quality_test(current_board, count):
    global ans
    for j in range(W):
        counts = 1
        for i in range(1, D):
            if current_board[i][j] == current_board[i-1][j]:
                counts += 1
                if counts == K:
                    break
            else:
                counts = 1
        else:
            return
    ans = count


T = int(input())
for test_case in range(1, T+1):
    D, W, K = map(int, input().split())
    board = []
    for i in range(D):
        board.append(list(map(int, input().split())))

    if K == 1:
        print(f'#{test_case} {0}')
        continue

    ans = K
    test_board = deepcopy(board)
    change(test_board, 0, 0)

    print(f'#{test_case} {ans}')
