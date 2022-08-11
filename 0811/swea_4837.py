T = int(input())

for test_case in range(1, T+1):
    N, K = list(map(int, input().split()))
    nums = list(range(1,13))
    ans = 0

    for i in range(1<<12):  # 2의 12제곱개를 모두 확인
        comb = []
        for j in range(12):  # 모든 원소에 대해
            if i & (1<<j):  # 해당 원소를 포함하는지 확인하는 비트연산
                comb.append(nums[j])  # 부분집합을 만든다
        if len(comb) == N:  # 크기조건
            if sum(comb) == K:  # 합조건
                ans = ans + 1  # 모두 만족시 정답+1

    print(f'#{test_case} {ans}')