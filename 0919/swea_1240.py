T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    flag = False
    for _ in range(N):
        line = input()
        if flag:
            continue
        if '1' in line[::-1]:
            last_idx = line[::-1].index('1')
            last_idx = M - last_idx - 1
            target = line[last_idx-55:last_idx+1]
            flag = True
    code_list = {
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9
    }
    check = 0
    ans = 0
    for i in range(8):
        number_code = code_list[target[7*i:7*i+7]]
        if not i % 2:
            check += number_code * 3
        else:
            check += number_code
        ans += number_code

    if check % 10:
        ans = 0
    print(f'#{test_case} {ans}')