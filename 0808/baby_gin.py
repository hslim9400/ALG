T = int(input())

for test_case in range(1, T+1):
    num = int(input())
    nums = []
    for _ in range(6):
        nums = [num % 10] + nums
        num = num//10

    counts = [0] * 12

    for i in range(len(nums)):
        counts[nums[i]] = counts[nums[i]] + 1

    while True:
        for i in range(len(counts)):
            if counts[i] >= 3:
                counts[i] = counts[i] -3
                break
        else:
            break

    while True:
        for i in range(len(counts)):
            if (counts[i] >= 1) and (counts[i+1] >= 1) and (counts[i+2] >= 1):
                counts[i], counts[i+1], counts[i+2] = counts[i] - 1, counts[i+1] - 1, counts[i+2] - 1
                break
        else:
            break

    print(counts)
    if sum(counts) == 0:
        ans = 'Baby Gin'
    else:
        ans = 'Lose'

    print(f'#{test_case} {ans}')


