T = int(input())

for test_case in range(T):

    nums = list(map(int, input().split()))
    subset = []
    ans = 0
    for i in range(1<<10):
        set_sum = 0
        if i == 0:
            continue
        for j in range(10):
            if i&(1<<j):
                set_sum = set_sum + nums[j]
        if set_sum == 0:
            ans = 1
            break
    print(f'#{test_case} {ans}')
