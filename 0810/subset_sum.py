T = int(input())

for test_case in range(T):

    nums = list(map(int, input().split()))
    subset = []
    ans = 0
    for i in range(1<<10):  # 원소가 열개인 집합의 모든 부분집합을 확인 할 예정
        set_sum = 0
        if i == 0:  # i 가 0이라면 공집합임
            continue
        for j in range(10):  # 모든 원소의 인덱스를 돌며
            '''
            2의 10제곱까지의 모든 자연수를 2의 9제곱까지의 제곱수의 합으로 표현할 수 있으며 표현방법이 유일하다.
            예를 들어 6은 2진법으로 110인데 4+2라는 뜻.
            3개의 원소를 가진 집합의 부분집합은 8개인데 이 중 여섯번째 부분집합은
            두번째와 세번째 원소를 원소로하는 집합이다.
            '''
            if i&(1<<j):
                set_sum = set_sum + nums[j]
        if set_sum == 0:  # 부분집합의 합이 0일경우 종료
            ans = 1
            break
    print(f'#{test_case} {ans}')
