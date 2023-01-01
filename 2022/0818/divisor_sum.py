def solution(left, right):
    answer = 0
    nums = list(range(left, right + 1))
    for num in nums:
        if int(num ** (0.5)) ** 2 == num:
            answer -= num
        else:
            answer += num

    return answer