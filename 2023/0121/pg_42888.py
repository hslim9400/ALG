def solution(record):
    answer = []
    nicknames = {}
    for log in record:
        log = log.split()
        if log[0] == 'Enter':
            nicknames[log[1]] = log[2]
        elif log[0] == 'Change':
            nicknames[log[1]] = log[2]

    for log in record:
        log = log.split()
        nickname = nicknames[log[1]]
        if log[0] == 'Enter':
            answer.append(f'{nickname}님이 들어왔습니다.')
        elif log[0] == 'Leave':
            answer.append(f'{nickname}님이 나갔습니다.')


    return answer

