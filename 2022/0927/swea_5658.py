def decode(target):
    global nums
    for i in range(4):
        side = ''.join(target[i*(N//4):(i+1)*(N//4)])
        nums.add(int('0x'+side, 16))
    return

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    code = list(input())
    nums = set()
    for i in range(N//4):
        code = ([code[-1]] + code)[:-1]
        decode(code)
    nums = list(nums)
    nums.sort(reverse=True)
    password = nums[K-1]
    print(f'#{test_case} {password}')
