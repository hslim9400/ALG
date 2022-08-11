T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    ans = []

    for i in range(len(nums)//2):
        ans.append(nums.pop(nums.index(max(nums))))
        ans.append(nums.pop(nums.index(min(nums))))

    ans = ans[:10]
    print(f'#{test_case}', *ans)