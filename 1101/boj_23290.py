fish_d = [0, [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
shark_d = [0, [-1, 0], [0, -1], [1, 0], [0, 1]]


def one(board):
    clones = {}
    for space in board.keys():
        if board[space]['fish']:
            clones[space] = board[space]['fish']
    return clones


def two(board):
    new_board = {}
    for i in range(1, 5):
        for j in range(1, 5):
            new_board[(i, j)] = {'fish': [], 'smell': 0}
    for space in board.keys():
        r, c = space[0], space[1]
        if board[space]['fish']:
            for _ in range(len(board[space]['fish'])):
                d = board[space]['fish'].pop()
                for _ in range(8):
                    nr, nc = r+fish_d[d][0], c+fish_d[d][1]
                    if 1 <= nr <= 4 and 1 <= nc <= 4 and not board[(nr, nc)]['smell'] and [nr, nc] != shark:
                            new_board[(nr, nc)]['fish'].append(d)
                            break
                    d += 1
                    d %= 9
                    if d == 0:
                        d += 1
                else:
                    new_board[(r, c)]['fish'].append(d)
    return new_board


def three(shark, board):
    max_counts = 0
    for d_1 in range(1, 5):
        for d_2 in range(1, 5):
            for d_3 in range(1, 5):

    return


def four():
    return


def five():
    return


M, S = map(int, input().split())
board = {}
for i in range(1, 5):
    for j in range(1, 5):
        board[(i, j)] = {'fish': [], 'smell': 0}
for _ in range(M):
    r, c, d = map(int, input().split())
    board[(r, c)]['fish'].append(d)
shark = list(map(int, input().split()))

for _ in range(S):
    clones = one(board)
