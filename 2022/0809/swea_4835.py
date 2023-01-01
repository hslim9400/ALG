
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N, M = list(map(int, input().split()))

    nums = list(map(int, input().split()))
    max_sum = 0  # 초기조건. 최대값은 0보다 클 것이므로
    min_sum = 1000000  # 초기조건. 최소값은 이 숫자보다 작다

    for i in range(N-M+1):
        num_sum = 0  # 구간합을 초기화
        for j in range(M):
            num_sum = num_sum + nums[i + j]  # i번째부터 i+M번째까지 구간합
        if num_sum > max_sum:  # 최대값보다 크면 갱신
            max_sum = num_sum
        if num_sum < min_sum:  # 최소값보다 작으면 갱신
            min_sum = num_sum

    print(f'#{test_case} {max_sum-min_sum}')
