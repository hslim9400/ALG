def melt():
    queue = [(0, 0)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    visited = []
    to_melt = set()
    while queue:
        current = queue.pop(0)
        r = current[0]
        c = current[1]
        if current in visited:
            continue
        visited.append(current)
        for d in range(4):
            if 0 <= r + dr[d] < N and 0 <= c + dc[d] < M:
                if board[r+dr[d]][c+dc[d]] == 0 and (r+dr[d], c+dc[d]) not in visited:
                    queue.append((r+dr[d], c+dc[d]))
                if board[r+dr[d]][c+dc[d]] == 1:
                    to_melt.add((r+dr[d], c+dc[d]))

    return to_melt



N, M = map(int, input().split())
board = []
cheeses = set()
for i in range(N):
    line = list(map(int, input().split()))
    board.append(line)
    for j in range(M):
        if line[j] == 1:
            cheeses.add((i, j))

sec = 0
while True:
    melt_cheese = melt()
    if melt_cheese:
        sec += 1
        left_cheese = len(cheeses)
        for cheese in melt_cheese:
            cheeses.discard(cheese)
            board[cheese[0]][cheese[1]] = 0
    else:
        break
print(sec)
print(left_cheese)