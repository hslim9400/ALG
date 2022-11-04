def rotate(lattice):
    lattice = list(zip(*lattice[::-1]))
    return lattice[:]


origin = [
    [0, 0, 0.02, 0, 0],
    [0, 0.1, 0.07, 0.01, 0],
    [0.05, 0, 0, 0, 0],
    [0, 0.1, 0.07, 0.01, 0],
    [0, 0, 0.02, 0, 0]
]
lattices = [origin, rotate(origin), rotate(rotate(origin)), rotate(rotate(rotate(origin)))]


def snail(N):
    board = [[0]*N for _ in range(N)]
    snail = []
    place = (0, 0)
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    d = 0
    for _ in range(N*N):
        r, c = place
        board[r][c] = 1
        snail.append([(r, c), d])
        if 0 <= r+dr[d] < N and 0 <= c+dc[d] < N and not board[r+dr[d]][c+dc[d]]:
            place = (r+dr[d], c+dc[d])
        else:
            d += 1
            d %= 4
            place = (r+dr[d], c+dc[d])
    return snail[::-1]


def scatter(place, d):
    global board, ans
    dr = [0, -1, 0, 1]
    dc = [-1, 0, 1, 0]
    r, c = place[0] + dr[d], place[1] + dc[d]
    target = board[r][c]
    lattice = lattices[d]
    for i in range(5):
        for j in range(5):
            ratio = lattice[i][j]
            nr, nc = r-2+i, c-2+j
            if 0 <= nr < N and 0 <= nc < N:
                board[nr][nc] += int(board[r][c] * ratio)
            else:
                ans += int(board[r][c] * ratio)
            target -= int(board[r][c] * ratio)

    if 0 <= r+dr[d] < N and 0 <= c+dc[d] < N:
        board[r+dr[d]][c+dc[d]] += target
    else:
        ans += target
    board[r][c] = 0


N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
snail = snail(N)
ans = 0
for current in snail:
    place = current[0]
    d = current[1]
    scatter(place, d)

print(ans)

