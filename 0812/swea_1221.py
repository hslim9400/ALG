T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    case, N = input().split()
    N = int(N)
    nums = list(range(10))
    alien = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    signal = input().split()
    trans = []
    decoder = {}

    for i in range(10):
        decoder[nums[i]] = alien[i]
        decoder[alien[i]] = nums[i]

    for i in range(N):
        trans.append(decoder[signal[i]])

    trans.sort()
    for i in range(N):
        trans[i] = decoder[trans[i]]

    print(case)
    print(*trans)