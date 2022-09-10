def find_area(x, y):
    global area, board
    queue = [(x, y)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    while queue:
        current = queue.pop()
        if board[current[0]][current[1]] != 0:
            continue
        board[current[0]][current[1]] = 1
        area += 1
        next_steps = []
        for d in range(4):
            if 0 <= current[0]+dx[d] < N and 0 <= current[1]+dy[d] < M:
                next_steps.append((current[0]+dx[d], current[1]+dy[d]))
        for next_step in next_steps:
            if not board[next_step[0]][next_step[1]] and next_step not in queue:
                queue.append(next_step)
    return


M, N, K = map(int, input().split())
board = [[0]*M for _ in range(N)]

for i in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            board[x][y] = 1

areas = []
for x in range(N):
    for y in range(M):
        if not board[x][y]:
            area = 0
            find_area(x, y)
            areas.append(area)

areas.sort()
print(len(areas))
print(*areas)


