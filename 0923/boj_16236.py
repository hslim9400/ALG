from collections import deque


def bfs():
    queue = deque()
    queue.append(((shark[0], shark[1]), 0))
    visited = set()
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    count = 0
    targets = []
    dist = N * N
    while queue:
        current = queue.popleft()
        if current[0] in visited:
            continue
        visited.add(current[0])
        r, c, t = current[0][0], current[0][1], current[1]
        if t == dist + 1:
            count = dist
            break
        if board[r][c]:
            if board[r][c] < shark[2]:
                targets.append((r, c, board[r][c]))
                dist = t
                count = dist
        for d in range(4):
            if 0 <= r+dr[d] < N and 0 <= c+dc[d] < N and (r+dr[d], c+dc[d]) not in visited:
                if board[r+dr[d]][c+dc[d]] <= shark[2]:
                    queue.append(((r+dr[d], c+dc[d]), t+1))

    return count, targets


N = int(input())
board = []
shark = 0
fishes = set()
for i in range(N):
    line = list(map(int, input().split()))
    board.append(line)
    for j in range(N):
        if line[j] == 9:
            shark = [i, j, 2, 2]
            board[i][j] = 0
        elif line[j]:
            fishes.add((i, j, line[j]))

total_count = 0
while fishes:
    count, targets = bfs()
    targets.sort(key=lambda x: (x[0], x[1]))
    if count:
        target = targets[0]
        shark[0], shark[1] = target[0], target[1]
        shark[3] -= 1
        board[target[0]][target[1]] = 0
        if shark[3] == 0:
            shark[2] += 1
            shark[3] = shark[2]
        fishes.discard(target)
    else:
        break
    total_count += count

print(total_count)

