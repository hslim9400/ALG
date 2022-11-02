fish_d = [0, [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
shark_d = [0, [-1, 0], [0, -1], [1, 0], [0, 1]]


def one(board):
    clones = {}
    for space in board.keys():
        if board[space]['fish']:
            clones[space] = board[space]['fish'][:]
    return clones


def two(board):
    new_board = {}
    for i in range(1, 5):
        for j in range(1, 5):
            new_board[(i, j)] = {'fish': [], 'smell': board[(i, j)]['smell']}
    for space in board.keys():
        r, c = space[0], space[1]
        if board[space]['fish']:
            for _ in range(len(board[space]['fish'])):
                d = board[space]['fish'].pop()
                for _ in range(8):
                    nr, nc = r+fish_d[d][0], c+fish_d[d][1]
                    if 1 <= nr <= 4 and 1 <= nc <= 4 and not board[(nr, nc)]['smell'] and (nr, nc) != shark:
                            new_board[(nr, nc)]['fish'].append(d)
                            break
                    d -= 1
                    if d == 0:
                        d = 8
                else:
                    new_board[(r, c)]['fish'].append(d)
    return new_board


def three(shark, board):
    max_counts = 0
    moves = []
    for d_1 in range(1, 5):
        for d_2 in range(1, 5):
            for d_3 in range(1, 5):
                counts = 0
                n_r, n_c = shark
                visited = set()
                for move in [d_1, d_2, d_3]:
                    n_r, n_c = n_r + shark_d[move][0], n_c + shark_d[move][1]
                    visited.add((n_r, n_c))
                for space in visited:
                    if space not in board.keys():
                        break
                    counts += len(board[space]['fish'])
                else:
                    if counts > max_counts:
                        max_counts = counts
                        moves = [d_1, d_2, d_3]
                    elif not moves:
                        moves = [d_1, d_2, d_3]
    for move in moves:
        r, c = shark
        r, c = r+shark_d[move][0], c+shark_d[move][1]
        shark = (r, c)
        if board[shark]['fish']:
            board[shark]['fish'] = []
            board[shark]['smell'] = 3
    return shark, board


def four(board):
    for space in board.keys():
        if board[space]['smell']:
            board[space]['smell'] -= 1
    return board


def five(clone, board):
    for space in clone.keys():
        board[space]['fish'].extend(clone[space])
    return board


M, S = map(int, input().split())
board = {}
for i in range(1, 5):
    for j in range(1, 5):
        board[(i, j)] = {'fish': [], 'smell': 0}
for _ in range(M):
    r, c, d = map(int, input().split())
    board[(r, c)]['fish'].append(d)
shark = tuple(map(int, input().split()))

for _ in range(S):
    clones = one(board)
    board = two(board)
    shark, board = three(shark, board)
    board = four(board)
    board = five(clones, board)

fishes = 0
for space in board.keys():
    fishes += len(board[space]['fish'])
print(fishes)