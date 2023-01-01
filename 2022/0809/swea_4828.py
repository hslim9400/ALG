T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    nums = list(map(int, input().split()))

    # 모든 숫자를 확인할 것이므로 첫 숫자로 지정
    min_num = nums[0]
    max_num = nums[0]

    for i in range(len(nums)):
        if min_num > nums[i]:  # min보다 작을 시 갱신
            min_num = nums[i]
        if max_num < nums[i]:  # max보다 클 시 갱신
            max_num = nums[i]

    ans = max_num - min_num
    print(f'#{test_case} {ans}')