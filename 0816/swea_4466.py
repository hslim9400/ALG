T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    score_list = list(map(int, input().split()))
    score_list.sort()
    score_sum = sum(score_list[-K:])
    print(f'#{test_case} {score_sum}')
