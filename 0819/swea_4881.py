
def next_row(row, prev_sum):
    global visited, min_sum
    new_sum = prev_sum
    if row == N-1:
        for i in range(N):
            if i not in visited:
                new_sum += board[row][i]
        if min_sum > new_sum:
            min_sum = new_sum
        return

    for i in range(N):
        new_sum = prev_sum
        if i in visited:
            continue
        new_sum += board[row][i]
        if new_sum > min_sum:
            continue
        visited.append(i)
        next_row(row+1, new_sum)
        visited.remove(i)


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    min_sum = 9 * N
    visited = []
    next_row(0, 0)

    print(f'#{test_case} {min_sum}')

