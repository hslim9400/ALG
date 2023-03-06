def solution(a):
    answer = min(len(a), 2)
    possibles = [False] * len(a)
    left_min = a[0]
    for i in range(1, len(a)-1):
        number = a[i]
        if number < left_min:
            possibles[i] = True
            left_min = number
    right_min = a[-1]
    for i in range(len(a)-2, 0, -1):
        number = a[i]
        if number > right_min:
            if possibles[i]:
                answer += 1
        else:
            answer += 1
            right_min = number
                
    return answer