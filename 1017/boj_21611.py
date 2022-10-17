from collections import deque
def snail():
    global board
    current = N * N - 1
    r, c = 0, 0
    d = 0
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    while current:
        board[r][c] = current
        if 0 <= r+dr[d] < N and 0 <= c+dc[d] < N and not board[r+dr[d]][c+dc[d]]:
            r += dr[d]
            c += dc[d]
        else:
            d += 1
            d %= 4
            r += dr[d]
            c += dc[d]
        current -= 1


def explode(marbles):
    global points
    while True:
        targets = []
        l = len(marbles)
        start = 0
        counts = 0
        for i in range(1, l):
            if marbles[i] == marbles[i-1]:
                counts += 1
            else:
                if counts >= 4:
                    targets.append([start, counts])
                    start = i
                    counts = 1
                else:
                    start = i
                    counts = 1
        if counts >= 4:
            targets.append([start, counts])
        if not targets:
            return marbles
        pulled = 0
        for target in targets:
            counts = target[1]
            idx = target[0] - pulled
            for _ in range(counts):
                points += marbles[idx]
                del marbles[idx]
            pulled += counts


def transform(marbles):
    l = len(marbles)
    if l == 1:
        return [0]
    new_marbles = [0] * N**2
    counts = 1
    pointer = 1
    for i in range(2, l):
        if marbles[i] == marbles[i-1]:
            counts += 1
        if marbles[i] != marbles[i-1]:
            new_marbles[pointer] = counts
            pointer += 1
            new_marbles[pointer] = marbles[i-1]
            pointer += 1
            if pointer == N**2:
                return new_marbles
            counts = 1
    new_marbles[pointer] = counts
    pointer += 1
    new_marbles[pointer] = marbles[-1]
    for i in range(N**2-1, -1, -1):
        if new_marbles[i]:
            new_marbles = new_marbles[:i+1]
            break
    return new_marbles


N, M = map(int, input().split())
shark = ((N-1)//2, (N-1)//2)
board = [[0]*N for _ in range(N)]
snail()
marbles = [0]*N**2
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        marbles[board[i][j]] = line[j]
for i in range(N**2-1, -1, -1):
    if marbles[i]:
        marbles = marbles[:i+1]
        break
else:
    marbles = [0]

dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]
points = 0
for _ in range(M):
    d, dist = map(int, input().split())
    for k in range(1, dist+1):
        r, c = shark[0]+k*dr[d], shark[1]+k*dc[d]
        idx = board[r][c]
        if idx-k+1 > len(marbles)-1:
            break
        del marbles[idx-k+1]
    marbles = explode(marbles)
    marbles = transform(marbles)
print(points)

