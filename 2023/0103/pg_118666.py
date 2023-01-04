
def solution(survey, choices):
    answer = ''
    results = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    n = len(survey)
    for i in range(n):
        category = survey[i]
        choice = choices[i]

        if choice < 4:
            target = category[0]
            results[target] += 4 - choice
        if choice > 4:
            target = category[1]
            results[target] += choice - 4

    for a, b in [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]:
        if results[a] >= results[b]:
            answer += a
        else:
            answer += b

    return answer

print(solution(["TR", "RT", "TR"], [7, 1, 3]))