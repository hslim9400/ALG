def remake(num, k):  # num을 k진수로
    target = ''  # 숫자를 하나하나 붙여줄 것이므로 문자열로 취급
    while num:  # num이 0이 되면 종료
        temp = str(num % k)  # 현재 num을 k로 나눈 나머지를
        target = temp + target  # 맨 앞에 붙인다.
        num //= k  # 몫을 다음 연산으로 넘긴다.
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