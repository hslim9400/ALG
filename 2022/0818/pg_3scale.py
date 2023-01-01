def solution(n):
    k = 1
    nums = []
    while True:
        if k > n:
            break
        k = k * 3
        nums.append(0)

    for i in range(len(nums), -1, -1):
        while True:
            if n >= 3 ** i:
                n -= 3 ** i
                nums[i] += 1
            else:
                break
    nums = nums[::-1]
    answer = 0
    for i in range(len(nums)):
        answer += nums[i] * (3 ** i)

    return answer


print(solution(81))