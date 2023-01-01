def search(depth, cost):
    global min_cost, visited
    if depth == N:
        if cost < min_cost:
            min_cost = cost

    for i in range(N):
        if visited[i]:
            continue
        if cost + board[depth][i] > min_cost:
            continue
        visited[i] = 1
        search(depth+1, cost+board[depth][i])
        visited[i] = 0


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    board = []
    for i in range(N):
        board.append(list(map(int, input().split())))

    min_cost = 99 * N
    visited = [0] * N
    search(0, 0)
    print(f'#{test_case} {min_cost}')

