def solution(answers):
    answer = []
    count_1 = 0
    count_2 = 0
    count_3 = 0
    ans_1 = []
    ans_2 = []
    ans_3 = []
    for i in range(len(answers)):
        ans_1 = i % 5 + 1
        if not i % 2:
            ans_2 = 2
        else:
            if i % 8 == 1:
                ans_2 = 1
            elif i % 8 == 3:
                ans_2 = 3
            elif i % 8 == 5:
                ans_2 = 4
            else:
                ans_2 = 5
        if i%10 // 2 == 0:
            ans_3 = 3
        elif i%10 // 2 == 1:
            ans_3 = 1
        elif i%10 // 2 == 2:
            ans_3 = 2
        elif i%10 // 2 == 3:
            ans_3 = 4
        else:
            ans_3 = 5
        print(ans_1, ans_2, ans_3)
        if ans_1 == answers[i]:
            count_1 += 1
        if ans_2 == answers[i]:
            count_2 += 1
        if ans_3 == answers[i]:
            count_3 += 1
    max_count = max(count_1, count_2, count_3)
    if count_1 == max_count:
        answer.append(1)
    if count_2 == max_count:
        answer.append(2)
    if count_3 == max_count:
        answer.append(3)

    return answer

solution([1,2,3,4,4,2,3,4,1,3,2])