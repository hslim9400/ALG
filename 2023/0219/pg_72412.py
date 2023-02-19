def solution(info, query):
    answer = []
    language = {'cpp': set(), 'java': set(), 'python': set()}
    position = {'backend': set(), 'frontend': set()}
    carrier = {'junior': set(), 'senior': set()}
    soulfood = {'pizza': set(), 'chicken': set()}
    scores = {}
    properties = [language, position, carrier, soulfood, scores]
    for i in range(len(info)):
        person = info[i].split()
        for j in range(4):
            properties[j][person[j]].add(i)


    for condition in query:
        current = set(range(len(info)))
        condition = condition.split()
        property_idx = 0
        counts = 0
        for target in condition:
            if target == condition[-1]:
                for candidate_idx in current:
                    candidate = info[candidate_idx].split()
                    if int(candidate[-1]) >= int(target):
                        counts += 1
                continue
            if target == 'and':
                continue
            if target == '-':
                property_idx += 1
                continue
            current = current & properties[property_idx][target]
            property_idx += 1
        answer.append(counts)
    return answer

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
         ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])