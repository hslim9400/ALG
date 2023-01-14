def solution(today, terms, privacies):
    answer = []

    today = today.split('.')
    today_value = int(today[0])*12*28 + int(today[1])*28 + int(today[2])
    terms_dict = {}
    for term in terms:
        term_type, term_value = term.split()
        terms_dict[term_type] = int(term_value)*28

    counts = 0
    for privacy in privacies:
        counts += 1
        start, term_type = privacy.split()
        start = list(map(int, start.split('.')))
        start_value = start[0]*12*28 + start[1]*28 + start[2]
        end_value = start_value + terms_dict[term_type]
        if end_value <= today_value:
            answer.append(counts)

    return answer