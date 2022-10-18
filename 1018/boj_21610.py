dr = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dc = [0, -1, -1, 0, 1, 1, 1, 0, -1]

def move_cloud(d, s, clouds):
    new_clouds = set()
    while clouds:
        cloud = clouds.pop()
        r, c = cloud[0], cloud[1]
        nr, nc = r+s*dr[d], c+s*dc[d]
        nr %= N
        nc %= N
        new_clouds.add((nr, nc))
    return new_clouds


N, M = map(int, input().split())
board = []
for i in range(N):
    line = list(map(int, input().split()))
    board.append(line)

clouds = {(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)}
for _ in range(M):
    d, s = map(int, input().split())
    clouds = move_cloud(d, s, clouds)

    for cloud in clouds:
        board[cloud[0]][cloud[1]] += 1

    for cloud in clouds:
        r, c = cloud[0], cloud[1]
        for x, y in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            if 0 <= r+x < N and 0 <= c+y < N:
                if board[r+x][c+y]:
                    board[r][c] += 1
    new_clouds = set()
    for i in range(N):
        for j in range(N):
            if board[i][j] >= 2:
                if (i, j) not in clouds:
                    new_clouds.add((i, j))
                    board[i][j] -= 2

    clouds = new_clouds

water = 0
for i in range(N):
    for j in range(N):
        water += board[i][j]
print(water)