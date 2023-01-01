def solution(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        if signs[i]:
            answer += abs(absolutes[i])
        else:
            answer += -abs(absolutes[i])
    return answer