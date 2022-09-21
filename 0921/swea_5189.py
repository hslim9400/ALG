def visit(depth, used, current):
    global min_battery
    if depth == N:
        used_battery = used + adj[current][0]
        if used_battery < min_battery:
            min_battery = used_battery
        return

    for i in range(1, N):
        if check[i]:
            continue
        new_used = used + adj[current][i]
        if new_used > min_battery:
            continue
        check[i] = 1
        visit(depth+1, new_used, i)
        check[i] = 0


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    adj = []
    for i in range(N):
        adj.append(list(map(int, input().split())))

    check = [0] * N
    min_battery = 100 * N
    visit(1, 0, 0)
    print(f'#{test_case} {min_battery}')