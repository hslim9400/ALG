def solution(nums):
    answer = -1
    counts = 0
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                target = nums[i] + nums[j] + nums[k]
                for n in range(2, int(target ** 0.5) + 1):
                    if not (target % n):
                        break
                else:
                    counts += 1

    answer = counts

    return answer