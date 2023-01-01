def solution(N, stages):
    answer = []
    counts = [0] * (N+2)
    counts_sum = [0] * (N+2)
    for stage in stages:
        counts[stage] += 1
        counts_sum[stage] += 1
    for i in range(N+1, 0, -1):
        counts_sum[i-1] += counts_sum[i]
    fail_rates = []
    for i in range(1, N+1):
        if counts_sum[i]:
            fail_rates.append([i, counts[i]/counts_sum[i]])
        else:
            fail_rates.append([i, 0])
    fail_rates.sort(key= lambda x:x[1], reverse=True)
    for i in range(N):
        answer.append(fail_rates[i][0])
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))