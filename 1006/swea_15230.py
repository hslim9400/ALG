correct = 'abcdefghijklmnopqrstuvwxyz'
T = int(input())

for test_case in range(1, T+1):
    target = input()
    ans = 0
    while ans < len(target):
        if target[ans] != correct[ans]:
            break
        ans += 1
    print(f'#{test_case} {ans}')