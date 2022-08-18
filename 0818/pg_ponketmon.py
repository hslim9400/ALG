def solution(nums):
    N = len(nums)
    picks = []
    for i in nums:
        if i not in picks:
            picks.append(i)
        if len(picks) == N // 2:
            answer = N // 2
            break
    else:
        answer = len(picks)

    return answer