def solution(num):
    answer = 0
    while num > 1:
        if num % 2:
            num *= 3
            num += 1
        else:
            num //= 2
        if answer == 500:
            answer = -1
            break
        answer += 1
    return answer
