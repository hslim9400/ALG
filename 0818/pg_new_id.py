def solution(new_id):
    possible = list(range(10)) + ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                                  'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '-', '_',
                                  '.']
    target = list()
    for i in new_id:
        new_id = new_id.lower()

    for i in new_id:
        if i in possible:
            target.append(i)
    while True:
        for i in range(len(target) - 1):
            if target[i] == target[i + 1] == '.':
                del target[i]
                break
        else:
            break

    if target:
        if target[0] == '.':
            target = target[1:]
    if target:
        if target[-1] == '.':
            target = target[:-1]
    target = target[:15]
    if not target:
        target.append('a')

    while True:
        if 2 < len(target) < 16:
            break
        target.append(target[-1])

    answer = ''.join(target)
    return answer


print(solution("=.="))