from collections import deque
case = 0
while True:
    case += 1
    N = int(input())
    if not N:
        break
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    costs = [[9*N*N]*N for _ in range(N)]
    costs[0][0] = board[0][0]
    queue = deque()
    queue.append((0, 0))
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    while queue:
        r, c = queue.popleft()
        for d in range(4):
            if 0 <= r+dr[d] < N and 0 <= c+dc[d] < N:
                if costs[r+dr[d]][c+dc[d]] > costs[r][c] + board[r+dr[d]][c+dc[d]]:
                    costs[r+dr[d]][c+dc[d]] = costs[r][c] + board[r+dr[d]][c+dc[d]]
                    queue.append((r+dr[d], c+dc[d]))
    print(f'Problem {case}: {costs[N-1][N-1]}')
