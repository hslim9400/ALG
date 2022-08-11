T = int(input())

for test_case in range(1, T+1):
    N, K = list(map(int, input().split()))
    nums = list(range(1,13))
    ans = 0

    for i in range(1<<12):
        comb = []
        for j in range(12):
            if i & (1<<j):
                comb.append(nums[j])
        if len(comb) == N:
            if sum(comb) == K:
                ans = ans + 1

    print(f'#{test_case} {ans}')