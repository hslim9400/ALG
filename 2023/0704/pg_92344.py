def solution(board, skill):
    N, M = len(board), len(board[0])
    answer = 0
    prefix = [[0] * (N + 1) for _ in range(M + 1)]
    diff = [[0] * N for _ in range(M)]
    for current in skill:
        t, r1, c1, r2, c2, d = current
        if t == 1:
            d = -d
        prefix[r1][c1] += d
        prefix[r2 + 1][c2 + 1] += d
        prefix[r2 + 1][c1] -= d
        prefix[r1][c2 + 1] -= d

    diff[0][0] = prefix[0][0]
    for c in range(1, M):
        diff[0][c] = diff[0][c - 1] + prefix[0][c]
    for r in range(1, N):
        diff[r][0] = diff[r - 1][0] + prefix[r][0]

    for r in range(1, N):
        for c in range(M):
            diff[r][c] = diff[r - 1][c] + prefix[r][c]
    for r in range(N):
        for c in range(M):
            diff[r][c] = diff[r][c - 1] + prefix[r][c]
    for r in range(N):
        print(diff[r])

    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] + diff[r][c] > 0:
                answer += 1

    return answer