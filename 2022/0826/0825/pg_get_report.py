def solution(id_list, report, k):
    answer = []
    mail_list = {}
    for user in id_list:
        mail_list[user] = []
    N = len(id_list)
    counts_list = [0] * N
    report_set = set(report)
    for case in report_set:
        reporter, reported = case.split()
        counts_list[id_list.index(reported)] += 1
        mail_list[reported].append(reporter)

    answer = [0] * N
    for i in range(N):
        if counts_list[i] >= k:
            for banned in mail_list[id_list[i]]:
                answer[id_list.index(banned)] += 1

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))