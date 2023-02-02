def solution(numbers):
    answer = []
    for number in numbers:
        target = list(bin(number)[2:][::-1])
        for i in range(len(target)):
            if target[i] == '0':
                target[i] = '1'
                for j in range(i-1, -1, -1):
                    if target[j] == '1':
                        target[j] = '0'
                        break
                break
        else:
            target = target[:-1] + ['0', '1']
        answer.append(int('0b'+''.join(target[::-1]), 2))

    return answer

print(solution([0, 1, 2, 3, 4, 5, 6,  7, 8, 9, 10]))