T = int(input())

for test_case in range(1, T+1):

    fees = list(map(int, input().split()))
    plan = list(map(int, input().split()))

    calenders = [[0]*12 for _ in range(2)]
    for i in range(12):
        calenders[0][i] = min(plan[i] * fees[0], fees[1])

    calenders[1][0] = calenders[0][0]
    calenders[1][1] = calenders[1][0] + calenders[0][1]
    if calenders[1][1] + calenders[0][2] > fees[2]:
        calenders[1][2] = fees[2]
    else:
        calenders[1][2] = calenders[1][1] + calenders[0][2]

    for i in range(3, 12):
        calenders[1][i] = min(calenders[1][i-1]+calenders[0][i], fees[2]+calenders[1][i-3])

    ans = min(calenders[1][-1], fees[3])

    print(f'#{test_case} {ans}')

