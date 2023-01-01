def solution(N, number):
    answer = 0
    dp = [0, {N}]
    if N == number:
        return 1
    for i in range(2, 9):
        new_set = set()
        new_set.add(int(str(N)*i))
        for p in range(1, 1+len(dp)//2):
            for target1 in dp[p]:
                for target2 in dp[i-p]:
                    new_set.add(target1+target2)
                    new_set.add(target1*target2)
                    new_set.add(target1-target2)
                    new_set.add(target2-target1)
                    if target2:
                        new_set.add(target1//target2)
                    if target1:
                        new_set.add(target2//target1)
        if number in new_set:
            answer = i
            break
        dp.append(new_set)
    else:
        answer = -1
    return answer
print(solution(5, 30525))
