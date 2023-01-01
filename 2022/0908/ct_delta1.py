T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    marbles = []
    dirs = {'U': 0, 'D': 3, 'R': 1, 'L': 2}

    for i in range(M):
        x, y, d = input().split()
        x, y = map(int, (x, y))
        d = dirs[d]
        marbles.append([x - 1, y - 1, d])
    counts = [[0] * N for _ in range(N)]
    dr = [-1, 0, 0, 1]
    dc = [0, 1, -1, 0]

    for _ in range(2 * N):
        new_marble = []
        for marble in marbles:
            r = marble[0]
            c = marble[1]
            d = marble[2]
            if 0 <= r + dr[d] < N and 0 <= c + dc[d] < N:
                marble[0] = r + dr[d]
                marble[1] = c + dc[d]
            else:
                marble[2] = 3 - marble[2]
            counts[marble[0]][marble[1]] += 1
        for marble in marbles:
            r = marble[0]
            c = marble[1]
            if counts[r][c] == 1:
                new_marble.append([marble[0], marble[1], marble[2]])
            counts[r][c] = 0
        marbles = new_marble

    print(len(marbles))


