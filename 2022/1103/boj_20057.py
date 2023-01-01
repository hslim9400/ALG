def rotate(lattice):  # 비율 배열을 돌리기 위한 함수
    lattice = list(zip(*lattice[::-1]))
    return lattice[:]


origin = [  # 최초의 비율 배열
    [0, 0, 0.02, 0, 0],
    [0, 0.1, 0.07, 0.01, 0],
    [0.05, 0, 0, 0, 0],
    [0, 0.1, 0.07, 0.01, 0],
    [0, 0, 0.02, 0, 0]
]
# 0번부터 3번까지 배열을 돌린 녀석을 인덱스에 맞게 넣는다.
lattices = [origin, rotate(origin), rotate(rotate(origin)), rotate(rotate(rotate(origin)))]


def snail(N):  # 달팽이를 돌며 움직일 순서대로 배열에 넣어준다.
    # 완성된 snail배열은 중앙부터 좌표, 방향을 담은 리스트가 될 것.
    # 5*5 보드 기준으로 [[(2,2), 0], [(2, 1), 1], ..] 이런 식
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

# 안녕하세요
def scatter(place, d):  # 현재 좌표와 방향을 받아 모래를 뿌리는 함수
    global board, ans
    dr = [0, -1, 0, 1]
    dc = [-1, 0, 1, 0]
    r, c = place[0] + dr[d], place[1] + dc[d]  # 타겟 모래 위치
    target = board[r][c]  # 남을 모래를 계산할 변수
    lattice = lattices[d]  # 방향에 맞는 비율 배열
    for i in range(5):  # 비율 배열을 돌며 비율을 곱하고 보드를 변경
        for j in range(5):
            ratio = lattice[i][j]
            nr, nc = r-2+i, c-2+j
            if 0 <= nr < N and 0 <= nc < N:
                board[nr][nc] += int(board[r][c] * ratio)
            else:
                ans += int(board[r][c] * ratio)
            target -= int(board[r][c] * ratio)

    if 0 <= r+dr[d] < N and 0 <= c+dc[d] < N:  # 알파가 들어갈 곳이 있다면 알파를 더하고 아니라면 답에 더함
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

