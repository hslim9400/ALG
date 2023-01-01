T = int(input())
for test_case in range(1, T+1):
    N, k_min, k_max = map(int, input().split())
    score_list = list(map(int, input().split()))

    min_score = min(score_list)
    max_score = max(score_list)
    min_diff = N

    for T_1 in range(min_score, max_score):
        for T_2 in range(T_1, max_score+1):
            A = []
            B = []
            C = []
            for score in score_list:
                if score < T_1:
                    A.append(score)
                elif score < T_2:
                    B.append(score)
                else:
                    C.append(score)
            if max(len(A), len(B), len(C)) > k_max or  min(len(A), len(B), len(C)) < k_min:
                continue
            diff = max(len(A), len(B), len(C)) - min(len(A), len(B), len(C))
            if diff < min_diff:
                min_diff = diff

    if min_diff == N:
        ans = -1
    else:
        ans = min_diff
    print(f'#{test_case} {ans}')
