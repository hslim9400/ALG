from collections import deque

T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    costs = [[1000*N*N]*N for _ in range(N)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    costs[0][0] = 0
    queue = deque()
    queue.append((0, 0))

    while queue:
        current = queue.popleft()
        r, c = current
        for d in range(4):
            if 0 <= r+dr[d] < N and 0 <= c+dc[d] < N:
                cost = 1
                if board[r][c] < board[r+dr[d]][c+dc[d]]:
                    cost += abs(board[r+dr[d]][c+dc[d]] - board[r][c])
                if costs[r+dr[d]][c+dc[d]] > costs[r][c] + cost:
                    costs[r+dr[d]][c+dc[d]] = costs[r][c] + cost
                    queue.append((r+dr[d], c+dc[d]))

    print(f'#{test_case} {costs[N-1][N-1]}')
