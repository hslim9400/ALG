def solution(today, terms, privacies):
    answer = []
    today = list(map(int, (today.split('.'))))
    terms_dic = {}
    for term in terms:
        term = term.split()
        terms_dic[term[0]] = int(term[1])

    for i in range(len(privacies)):
        privacy = privacies[i]
        start, term = privacy.split()
        start = list(map(int, (start.split('.'))))
        end = start[:]
        end[1] += terms_dic[term]
        end[0] += (end[1] - 1) // 12
        end[1] = (end[1] - 1) % 12 + 1
        if end[2] == 1:
            if end[1] == 1:
                end[0] -= 1
                end[1] = 12
                end[2] = 28
            else:
                end[1] -= 1
                end[2] = 28
        else:
            end[2] -= 1
        for j in range(3):
            if end[j] < today[j]:
                answer.append(i + 1)
                break

    return answer

print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
