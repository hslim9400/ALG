def solution(s):
    answer = []
    alps = {}
    for i in range(len(s)):
        letter = s[i]
        if letter in alps.keys():
            answer.append(i-alps[letter])
        else:
            answer.append(-1)
        alps[letter] = i

    return answer
print(solution("foobar"))