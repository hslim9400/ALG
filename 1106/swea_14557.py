
T = int(input())
for test_case in range(1, T+1):
    target = input()
    if not target.count('1'):
        print(f'#{test_case} no')
        continue
    if target.count('1') % 2:
        print(f'#{test_case} yes')
    else:
        print(f'#{test_case} no')
