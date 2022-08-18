def solution(price, money, count):
    total = 0
    for i in range(1, count+1):
        total += i * price
    answer = money - total
    if answer > 0:
        answer = 0

    return abs(answer)