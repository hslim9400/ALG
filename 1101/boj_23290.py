# 정직한 구현과 직관적인 함수이름을 통한 문제해결
fish_d = [0, [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
shark_d = [0, [-1, 0], [0, -1], [1, 0], [0, 1]]


def one(board):  # 1번 구현. 물고기들 복제하기
    clones = {}
    for space in board.keys():
        if board[space]['fish']:
            clones[space] = board[space]['fish'][:]
    return clones


def two(board):  # 2번 구현. 물고기들 이동하기
    new_board = {}
    for i in range(1, 5):
        for j in range(1, 5):
            new_board[(i, j)] = {'fish': [], 'smell': board[(i, j)]['smell']}
    for space in board.keys():  # 모든 가상좌표에 대해
        r, c = space[0], space[1]
        if board[space]['fish']:  # 물고기가 있다면
            for _ in range(len(board[space]['fish'])):  # 물고기를 모두 옮김
                d = board[space]['fish'].pop()
                for _ in range(8):
                    nr, nc = r+fish_d[d][0], c+fish_d[d][1]
                    if 1 <= nr <= 4 and 1 <= nc <= 4 and not board[(nr, nc)]['smell'] and (nr, nc) != shark:  # 물고기 냄새와 상어를 피함
                            new_board[(nr, nc)]['fish'].append(d)
                            break  # 옮겼다면 다음 물고기
                    d -= 1
                    if d == 0:
                        d = 8
                else:  # 움직이지 않았다면 제자리
                    new_board[(r, c)]['fish'].append(d)
    return new_board


def three(shark, board):  # 3번 구현. 물고기 없애기
    max_counts = 0
    moves = []
    for d_1 in range(1, 5):  # 중복순열로 세번의 이동 완전탐색
        for d_2 in range(1, 5):
            for d_3 in range(1, 5):
                counts = 0
                n_r, n_c = shark
                visited = set()  # 같은 자리를 갈 수 있되 물고기를 두번 세지는 않도록
                for move in [d_1, d_2, d_3]:
                    n_r, n_c = n_r + shark_d[move][0], n_c + shark_d[move][1]
                    visited.add((n_r, n_c))
                for space in visited:
                    if space not in board.keys():  # 지도를 벗어남
                        break
                    counts += len(board[space]['fish'])  # 물고기의 개수
                else:  # 브레이크가 걸렸다면 유효한 이동이 아니므로
                    if counts > max_counts:  # 사전순으로 움직이므로
                        # 최대 물고기와 같다면 먼저 나온 움직임이 바른 이동
                        max_counts = counts
                        moves = [d_1, d_2, d_3]
                    elif not moves:
                        moves = [d_1, d_2, d_3]
    for move in moves:  # 움직이며 물고기를 없애고 냄새를 남긴다.
        r, c = shark
        r, c = r+shark_d[move][0], c+shark_d[move][1]
        shark = (r, c)
        if board[shark]['fish']:
            board[shark]['fish'] = []
            board[shark]['smell'] = 3  # 2번에서 생긴 냄새가 다다음 4번에서 지워지므로 이번 턴의 4번 후 냄새가 2 남아야 함
    return shark, board


def four(board):  # 4번 구현. 냄새 지우기
    for space in board.keys():
        if board[space]['smell']:
            board[space]['smell'] -= 1
    return board


def five(clone, board):  # 5번 구현. 복제한 물고기 들여오기
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

for _ in range(S):  # S만큼 1번부터 5번 시행
    clones = one(board)
    board = two(board)
    shark, board = three(shark, board)
    board = four(board)
    board = five(clones, board)

fishes = 0
for space in board.keys():
    fishes += len(board[space]['fish'])
print(fishes)