def solution(numbers):
    answer = []
    for number in numbers:
        # 뒤부터 확인하며 0을 만나면 1로 바꾸고
        # 그 숫자로부터 다시 뒤로가며 1을 만나면 0으로 바꿈
        # 만약 모두 1이라면 가장 앞의 1을 10으로 바꿈
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