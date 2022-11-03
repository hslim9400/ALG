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
    global board
    dr = [0, -1, 0, 1]
    dc = [-1, 0, 1, 0]
    r, c = place
    targets = [()]


N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
snail = snail(N)
print(snail)
for current in snail:
    place = current[0]
    d = current[1]

