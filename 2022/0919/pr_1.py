T = int(input())
for test_case in range(1, T+1):
    target = input()
    N = len(target)
    nums = []
    for i in range(N//7):
        bin_num = target[7*i:7*i+7]
        num = 0
        for i in range(7):
            num += (2 ** i) * int(bin_num[-1-i])
        nums.append(num)
    print(*nums)