T = int(input())
for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    customers = list(map(int, input().split()))
    customers.sort()
    for i in range(N-1):
        for j in range(i+1, N):
            customers[j] -= customers[i]
    now = 0
    savings = 0
    next_bread = M
    for i in range(N):
        while True:
            cycle_time = min(next_bread, customers[i])
            now += cycle_time
            next_bread -= cycle_time
            if next_bread == 0:
                savings += K
                next_bread = M
            customers[i] -= cycle_time
            if customers[i] == 0:
                break
        if savings == 0:
            ans = 'Impossible'
            break
        else:
            savings -= 1
    else:
        ans = 'Possible'
    print(f'#{test_case} {ans}')
