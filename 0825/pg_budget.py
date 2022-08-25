def solution(d, budget):
    answer = 0
    d.sort()
    counts = 0
    for ask in d:
        budget -= ask
        if budget < 0:
            break
        counts += 1
    answer = counts

    return answer