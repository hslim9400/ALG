def solution(s):
    n = len(s)
    answer = n
    for k in range(1, n // 2 + 1):
        clone = s
        new_s = ['']
        counts = [1]
        while clone:
            if clone[:k] == new_s[-1]:
                counts[-1] += 1
                clone = clone[k:]
            else:
                new_s.append(clone[:k])
                counts.append(1)
                clone = clone[k:]
        for i in range(len(counts)):
            if counts[i] > 1:
                new_s[i] = str(counts[i]) + new_s[i]
        new_s = ''.join(new_s)
        if answer > len(new_s):
            answer = len(new_s)

    return answer