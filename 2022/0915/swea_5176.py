def mid(target):
    global nums, num
    if left[target]:
        mid(left[target])
    nums[target] = num
    num += 1
    if right[target]:
        mid(right[target])


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    left = [0] * (N+1)
    right = [0] * (N+1)
    for i in range(1, N//2+1):
        left[i] = 2*i
        if 2*i + 1 > N:
            continue
        right[i] = 2*i + 1

    nums = [0] * (N+1)
    num = 1
    mid(1)

    print(f'#{test_case} {nums[1]} {nums[N//2]}')
