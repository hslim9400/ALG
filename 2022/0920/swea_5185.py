T = int(input())
for test_case in range(1, T+1):
    N, target = input().split()
    num = bin(int(target, 16))[2:]
    ans = '0' * (len(target) * 4 - len(num)) + num
    print(f'#{test_case} {ans}')