T = int(input())
for test_case in range(1, T+1):
    N, M, C = map(int, input().split())
    board = []
    for i in range(N):
        line = list(map(int, input().split()))
        board.append(line)

    max_profit = 0
    for i in range(N):
        for j in range(N-M+1):
            profit = 0
            target = board[i][j:j+M]
            target.sort(reverse=True)
            honey = 0
            for k in range(1<<M):
                selected = []
                current = 0
                for l in range(M):
                    if k & (1<<l):
                        selected.append(target[l])
                        if sum(selected) > C:
                            selected = []
                            break
                if not selected:
                    continue
                for num in selected:
                    current += num**2
                if current > profit:
                    profit = current
            for i_2 in range(i, N):
                for j_2 in range(N-M+1):
                    second = 0
                    if i_2 == i and (j-M+1 <= j_2 <= j+M-1):
                        continue
                    target = board[i_2][j_2:j_2+M]
                    target.sort(reverse=True)
                    honey = 0
                    for k in range(1 << M):
                        selected = []
                        current = 0
                        for l in range(M):
                            if k & (1 << l):
                                selected.append(target[l])
                                if sum(selected) > C:
                                    selected = []
                                    break
                        if not selected:
                            continue
                        for num in selected:
                            current += num ** 2
                        if current > second:
                            second = current
                    if second + profit > max_profit:
                        max_profit = second + profit

    print(f'#{test_case} {max_profit}')