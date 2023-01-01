T = int(input())
for test_case in range(1, T+1):
    nums = list(map(int, input().split()))
    sums = []
    for i in range(5):
        for j in range(i+1, 6):
            for k in range(j+1, 7):
                sums.append(sum([nums[i], nums[j], nums[k]]))
    sums = list(set(sums))
    sums.sort()
    print(f'#{test_case} {sums[-5]}')
