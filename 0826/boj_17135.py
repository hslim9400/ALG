from copy import deepcopy


def one_round(round, archers, board):
    global counts
    if round == N:
        return

    new_board = deepcopy(board)
    got_shot = []
    for k in range(3):
        dist = 1
        flag = True
        while dist <= D and flag:
            attacked = []
            for i in range(N-1, -1, -1):
                if not flag:
                    break
                for j in range(M):
                    if abs(archers[k] - j) + abs(N - i) == dist:
                        attacked.append((i, j))
            attacked.sort(key=lambda x:x[1])
            for i in range(len(attacked)):
                if board[attacked[i][0]][attacked[i][1]] == 1:
                    if (attacked[i][0], attacked[i][1]) not in got_shot:
                        counts += 1
                        got_shot.append((attacked[i][0], attacked[i][1]))
                    flag = False
                    break
            dist += 1
    for i in range(len(got_shot)):
        new_board[got_shot[i][0]][got_shot[i][1]] = 0
    for i in range(N-1, 0, -1):
        new_board[i] = new_board[i-1]
    new_board[0] = [0] * M

    one_round(round+1, archers, new_board)


N, M, D = map(int, input().split())
board = []
for i in range(N):
    board.append(list(map(int, input().split())))

max_count = 0
for arc_1 in range(M-2):
    for arc_2 in range(arc_1+1, M-1):
        for arc_3 in range(arc_2+1, M):
            clone = deepcopy(board)
            counts = 0
            one_round(0, (arc_1, arc_2, arc_3), clone)
            if counts > max_count:
                max_count = counts
print(max_count)
