T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    num_list = ''
    while True:
        line = input().split()
        num_list += ''.join(line)
        if len(num_list) == N:
            break

    check = 0
    while True:
        if str(check) not in num_list:
            break
        check += 1
    print(f'#{test_case} {check}')
    