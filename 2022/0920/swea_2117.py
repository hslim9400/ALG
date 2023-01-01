def cover(center, dist):

    r = center[0]
    c = center[1]
    covered = set()
    for dr in range(dist):
        for dc in range(dist-dr):
            if r + dr < N and c + dc < N:
                if board[r+dr][c+dc]:
                    covered.add((r+dr, c+dc))
            if r + dr < N and c - dc >= 0:
                if board[r+dr][c-dc]:
                    covered.add((r+dr, c-dc))
            if r - dr >= 0 and c + dc < N:
                if board[r-dr][c+dc]:
                    covered.add((r-dr, c+dc))
            if r - dr >= 0 and c - dc >= 0:
                if board[r-dr][c-dc]:
                    covered.add((r-dr, c-dc))

    return len(covered)


T = int(input())
for test_case in range(1, T+1):

    N, M = map(int, input().split())
    board = []
    homes = 0
    for i in range(N):
        line = list(map(int, input().split()))
        board.append(line)
        for j in line:
            if j == 1:
                homes += 1

    max_covered = 0
    for k in range(1, 2*N+1):
        money = k * k + (k-1)*(k-1)
        if money > M * homes:
            break
        for i in range(N):
            for j in range(N):
                covered_homes = cover((i, j), k)
                if money > M * covered_homes:
                    continue
                if covered_homes > max_covered:
                    max_covered = covered_homes
        if max_covered == homes:
            break

    print(f'#{test_case} {max_covered}')
