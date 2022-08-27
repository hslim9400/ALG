def make_bin(n):
    bin_num = ''
    while n:
        bin_num = str(n % 2) + bin_num
        n //= 2
    return bin_num


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    target = make_bin(M)
    if target[::-1][:N] == '1' * N:
        ans = 'ON'
    else:
        ans = 'OFF'
    print(f'#{test_case} {ans}')
