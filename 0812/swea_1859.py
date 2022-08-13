T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    total_cost = list(map(int,input().split()))
    end = total_cost[-1]
    total_gain = 0
    while True:
        max_cost = max(total_cost)
        max_index = total_cost.index(max_cost)
        # 산 모든 물건들의 이익은 (최댓값 - 물건)의 가격이므로 최댓값을 일수만큼 곱하고
        # 물건들의 가격합하여 빼준다
        total_gain += max_cost*max_index-sum(total_cost[:max_index])
        if total_cost[max_index] == end:  # 종료조건, 마지막날이 되었으므로
            break
        total_cost = total_cost[max_index+1:]
    print(f'#{test_case} {total_gain}')