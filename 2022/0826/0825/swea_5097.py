T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    for i in range(M):  # M번 수행
        move = nums.pop(0)  # 가장 앞의 숫자를 꺼내서
        nums.append(move)  # 뒤에 붙인다.
    print(f'#{test_case} {nums[0]}')