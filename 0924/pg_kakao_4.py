def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        if numbers[i] == 1:
            answer.append(1)
            continue
        target = bin(numbers[i])[2:]
        k = 0
        while True:
            if 2 ** k > len(target):
                target = '0' * (2 ** k - len(target) - 1) + target
                level = k
                break
            k += 1
        checks = [2 ** (level - 1)]
        stride = 2 ** (level - 2)
        check = 1
        flag = False
        while True:
            if check == level+1:
                answer.append(1)
                break
            if flag:
                answer.append(0)
                break
            for j in range(len(checks)):
                idx = checks[j] - 1
                if target[idx] == '0':
                    if target[idx - stride] == '1':
                        flag = True
                        break
                    if target[idx + stride] == '1':
                        flag = True
                        break
                checks.append(idx + 1 - stride)
                checks.append(idx + 1 + stride)
            checks = checks[check:]
            check += 1
            stride //= 2

    return answer

print(solution([1,2,3,4,5,6,7,8,9,10, 11, 12, 13, 14, 15, 16]))
