def remake(num, k):
    target = ''
    while num:
        temp = str(num % k)
        target = temp + target
        num //= k
    return target


def solution(n, k):
    answer = -1
    num = remake(n, k)
    num = num.split('0')
    primes = []
    print(num)
    for i in range(len(num)):
        if not num[i]:
            continue
        if num[i] == '1':
            continue
        target = int(num[i])
        for j in range(2, int(target ** 0.5) + 1):
            if not target % j:
                print(target, j)
                break
        else:
            primes.append(target)
    print(primes)
    if primes:
        answer = len(primes)

    return answer

print(solution(10203040506070809, 10))