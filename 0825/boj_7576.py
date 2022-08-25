from collections import deque

M, N = map(int, input().split())
board = []
queue = deque([])
zeros = 0
for i in range(N):
    line = list(map(int, input().split()))
    board.append(line)
    for j in range(M):
        if board[i][j] == 1:
            queue.append([(i, j), 0])
            board[i][j] = 0
            zeros += 1
        elif board[i][j] == 0:
            zeros += 1

days = 0
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

while queue:
    current = queue.popleft()
    current_loca = current[0]
    if board[current_loca[0]][current_loca[1]] != 0:
        continue
    if current[1] > days:
        days = current[1]
    board[current_loca[0]][current_loca[1]] = 1
    zeros -= 1
    next_steps = []
    for d in range(4):
        if 0 <= current_loca[0] + dr[d] < N and 0 <= current_loca[1] + dc[d] < M:
            next_steps.append((current_loca[0] + dr[d], current_loca[1] + dc[d]))
    for next_step in next_steps:
        if board[next_step[0]][next_step[1]] == 0:
            queue.append([next_step, current[1] + 1])


if zeros != 0:
    print(-1)
else:
    print(days)
