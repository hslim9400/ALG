def next_row(row, cost):
    global min_cost
    if row == N:
        if cost < min_cost:
            min_cost = cost
        return

    for i in range(N):
        new_cost = cost
        if check[i]:
            continue
        new_cost += factory[row][i]
        if new_cost > min_cost:
            continue
        check[i] = 1
        next_row(row+1, new_cost)
        check[i] = 0


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    factory = []
    for _ in range(N):
        factory.append(list(map(int, input().split())))
    min_cost = 99 * N
    check = [0] * N
    next_row(0, 0)
    print(f'#{test_case} {min_cost}')
