def solution(lottos, win_nums):
    rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    answer = []
    zero = lottos.count(0)
    counts = 0
    for i in lottos:
        if i in win_nums:
            counts += 1
    answer.append(rank[counts + zero])
    answer.append(rank[counts])

    return answer