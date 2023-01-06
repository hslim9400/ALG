def solution(alp, cop, problems):
    max_alp = 0
    max_cop = 0
    for problem in problems:
        max_alp = max(max_alp, problem[0])
        max_cop = max(max_cop, problem[1])
    alp, cop = min(max_alp, alp), min(max_cop, cop)

    dp = [[float('inf')] * (max_cop+1) for _ in range(max_alp+1)]
    print(dp)
    dp[alp][cop] = 0

    for al in range(alp, max_alp+1):
        for co in range(cop, max_cop+1):
            if al + 1 <= max_alp:
                dp[al+1][co] = min(dp[al+1][co], dp[al][co] + 1)
            if co + 1 <= max_cop:
                dp[al][co+1] = min(dp[al][co+1], dp[al][co] + 1)

            for problem in problems:
                if problem[0] <= al <= max_alp-problem[2] and problem[1] <= co <= max_cop-problem[3]:
                    dp[al+problem[2]][co+problem[3]] = min(dp[al+problem[2]][co+problem[3]], dp[al][co] + problem[4])

    print(dp)
    answer = dp[-1][-1]
    return answer

print(solution(0, 0, [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]))