dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dfs(i, j):
    global visited
    stack = [(i, j)]
    targets = set()
    while stack:
        current = stack.pop()
        r, c = current[0], current[1]
        if visited[r][c]:
            continue
        visited[r][c] = 1
        targets.add(current)
        for d in range(4):
            if 0 <= r+dr[d] < N and 0 <= c+dc[d] < N:
                if L <= abs(board[r][c] - board[r+dr[d]][c+dc[d]]) <= R and\
                        not visited[r+dr[d]][c+dc[d]]:
                    stack.append((r+dr[d], c+dc[d]))

    if len(targets) > 1:
        avg = 0
        for target in targets:
            avg += board[target[0]][target[1]]
        return avg//len(targets), targets
    else:
        return 0, set()


N, L, R = map(int, input().split())
board = []
for i in range(N):
    board.append(list(map(int, input().split())))

day = 0
while True:
    visited = [[0]*N for _ in range(N)]
    moved = 0
    for i in range(N):
        for j in range(N):
            avg, targets = dfs(i, j)
            if avg:
                moved += 1
                for target in targets:
                    board[target[0]][target[1]] = avg
    if not moved:
        break
    day += 1
print(day)

