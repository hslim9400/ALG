def melt():  # bfs로 녹이기
    queue = [(0, 0)]  # 외각에 노출 된 치즈가 녹으므로 벽으로 시작한다.
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    visited = []
    to_melt = set()  # 녹을 치즈들의 좌표
    while queue:  # 공기의 좌표들을 돌되 공기와 접촉하는 치즈를 녹을 치즈에 추가
        current = queue.pop(0)
        r = current[0]
        c = current[1]
        if current in visited:
            continue
        visited.append(current)
        for d in range(4):
            if 0 <= r + dr[d] < N and 0 <= c + dc[d] < M:
                if board[r+dr[d]][c+dc[d]] == 0 and (r+dr[d], c+dc[d]) not in visited:  # 공기는 큐에 추가
                    queue.append((r+dr[d], c+dc[d]))
                if board[r+dr[d]][c+dc[d]] == 1:  # 치즈는 녹을 치즈에 추가
                    to_melt.add((r+dr[d], c+dc[d]))

    return to_melt  # 녹을 치즈 반환



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
    if melt_cheese:  # 녹을 치즈가 있다면
        sec += 1  # 시간이 흐르고
        left_cheese = len(cheeses)  # 마지막으로 녹는 치즈는 개수를 남겨야 함.
        for cheese in melt_cheese:  # 치즈를 녹인다.
            cheeses.discard(cheese)
            board[cheese[0]][cheese[1]] = 0
    else:
        break
print(sec)
print(left_cheese)