# dp[al][co] = al만큼의 알고리즘력, co만큼의 코딩력을 요구하는 문제를 푸는데 걸리는 최소시간
# 모든 문제를 순회하며 해당 문제를 풀게 됐을 경우 dp[al][co]를 갱신


def solution(alp, cop, problems):
    max_alp = 0
    max_cop = 0
    for problem in problems:
        max_alp = max(max_alp, problem[0])
        max_cop = max(max_cop, problem[1])
    alp, cop = min(max_alp, alp), min(max_cop, cop)

    dp = [[float('inf')] * (max_cop+1) for _ in range(max_alp+1)]
    # 최소시간을 갱신할것이니 무한대로 초기값 세팅
    dp[alp][cop] = 0
    # 처음 가진 알고력과 코딩력으로 풀 수 있는 문제는 0시간이 필요

    for al in range(alp, max_alp+1):
        for co in range(cop, max_cop+1):
            if al < max_alp:
                dp[al+1][co] = min(dp[al+1][co], dp[al][co] + 1)
            if co < max_cop:
                dp[al][co+1] = min(dp[al][co+1], dp[al][co] + 1)

            for problem in problems:
                if problem[0] <= al and problem[1] <= co:
                    al_temp, co_temp = min(max_alp, al+problem[2]), min(max_cop, co+problem[3])
                    dp[al_temp][co_temp] = min(dp[al_temp][co_temp], dp[al][co] + problem[4])

    answer = dp[max_alp][max_cop]
    return answer
