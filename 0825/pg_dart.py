def solution(dartResult):
    answer = 0
    trials = []
    dartResult = list(dartResult)
    bonus = {'S': 1, 'D': 2, 'T': 3}
    scores = []
    for i in range(len(dartResult)):
        if dartResult[i].isnumeric():
            if dartResult[i] == '0' and i:
                if dartResult[i-1] == '1':
                    trials[-1][0] = 10
                    continue
            trials.append([int(dartResult[i])])
        else:
            trials[-1].append(dartResult[i])
    print(trials)
    for trial in trials:
        base = trial[0]
        score = base ** bonus[trial[1]]
        if len(trial) == 3:
            if trial[2] == '#':
                score = -score
            else:
                score = 2 * score
                if scores:
                    scores[-1] = 2 * scores[-1]
        scores.append(score)
    answer = sum(scores)
    return answer


print(solution('1D2S#10S'))
