def roll(current_facing, move):
    # 주사위 굴리기
    if move == 0:
        current_facing['top'], current_facing['west'], current_facing['bottom'], current_facing['east'] = \
            current_facing['west'], current_facing['bottom'], current_facing['east'], current_facing['top']
    elif move == 1:
        current_facing['top'], current_facing['south'], current_facing['bottom'], current_facing['north'] = \
            current_facing['north'], current_facing['top'], current_facing['south'], current_facing['bottom']
    elif move == 2:
        current_facing['top'], current_facing['east'], current_facing['bottom'], current_facing['west'] = \
            current_facing['east'], current_facing['bottom'], current_facing['west'], current_facing['top']
    else:
        current_facing['top'], current_facing['south'], current_facing['bottom'], current_facing['north'] = \
            current_facing['south'], current_facing['bottom'], current_facing['north'], current_facing['top']
    return current_facing


def get_point(start):
    # 점수를 계산하는 dfs
    stack = [start]
    target = board[start[0]][start[1]]
    visited = set()
    point = 0
    while stack:
        current = stack.pop()
        r, c = current
        if current in visited:
            continue
        point += target
        visited.add(current)
        for d in range(4):
            nr, nc = r+dr[d], c+dc[d]
            if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == target:
                stack.append((nr, nc))
    return point


current_facing = {'bottom': 6, 'top': 1, 'east': 3, 'west': 4, 'south': 5, 'north': 2}
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
N, M, K = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

current = (0, 0, 0)
points = 0
for _ in range(K):
    r, c, d = current
    nr, nc = r+dr[d], c+dc[d]
    if 0 <= nr < N and 0 <= nc < M:
        current_facing = roll(current_facing, d)
        points += get_point((nr, nc))
        if current_facing['bottom'] > board[nr][nc]:
            d += 1
            d %= 4
        elif current_facing['bottom'] < board[nr][nc]:
            d -= 1
            d %= 4
    else:
        d += 2
        d %= 4
        nr, nc = r+dr[d], c+dc[d]
        current_facing = roll(current_facing, d)
        points += get_point((nr, nc))
        if current_facing['bottom'] > board[nr][nc]:
            d += 1
            d %= 4
        elif current_facing['bottom'] < board[nr][nc]:
            d -= 1
            d %= 4
    current = (nr, nc, d)

print(points)