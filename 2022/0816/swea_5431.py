T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    stu_list = list(range(1, N+1))
    hw_list = list(map(int, input().split()))

    for i in hw_list:
        stu_list.remove(i)

    print(f'#{test_case}', *stu_list)