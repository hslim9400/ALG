import heapq
def dijkstra():
    costs = [[10*N*N]*N for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    heap = []
    heapq.heappush(heap, (board[0][0], 0, 0))
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    while heap:
        cost, r, c = heapq.heappop(heap)
        if visited[r][c]:
            continue
        visited[r][c] = 1
        costs[r][c] = cost
        for d in range(4):
            if 0 <= r+dr[d] < N and 0 <= c+dc[d] < N and not visited[r+dr[d]][c+dc[d]]:
                if costs[r+dr[d]][c+dc[d]] > cost+board[r+dr[d]][c+dc[d]]:
                    heapq.heappush(heap, (cost+board[r+dr[d]][c+dc[d]], r+dr[d], c+dc[d]))
    return costs[N-1][N-1]

case = 0
while True:
    case += 1
    N = int(input())
    if not N:
        break
    board = []

    for _ in range(N):
        board.append(list(map(int, input().split())))

    print(f'Problem {case}: {dijkstra()}')

