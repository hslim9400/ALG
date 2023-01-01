T = int(input())
for test_case in range(1, T+1):
    target = float(input())
    ans = ''
    for i in range(1, 13):
        if target >= 2**(-i):
            target -= 2**(-i)
            ans += str(1)
        else:
            ans += str(0)
        if not target:
            break
    if target:
        ans = 'overflow'
    print(f'#{test_case} {ans}')