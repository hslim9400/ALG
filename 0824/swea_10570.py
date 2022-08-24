T = int(input())
for test_case in range(1, T+1):
    a, b = map(int, input().split())
    counts = 0
    for i in range(a, b+1):
        if (int(i**0.5))**2 == i and str(i) == str(i)[::-1] and\
                str(int(i**0.5)) == str(int(i**0.5))[::-1]:
            counts += 1

    print(f'#{test_case} {counts}')