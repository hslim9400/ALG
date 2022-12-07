
T = int(input())
for test_case in range(1, T+1):
    first = list(range(7))
    target = list(range(7))
    M, K = map(int, input().split())
    locations = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6}
    orders = []
    for _ in range(M):  # 한 사이클 돌려보기
        a, b = map(int, input().split())
        orders.append((a-1, b-1))
        target[a-1], target[b-1] = target[b-1], target[a-1]
    after_m = {}
    for i in range(7):  # M번(한 사이클) 돌았을 때 변하는 인덱스
        after_m[i] = target[i]
    cycle = 1
    while True:  # 처음으로 돌아오는데 몇 사이클을 돌아야 하는 지 파악
        cycle += 1
        new_target = list(range(7))
        for i in range(7):
            new_target[i] = target[after_m[i]]
        target = new_target
        if new_target == first:  # 처음으로 돌아왔다면 종료
            break

    left = K % (cycle*M)  # 남은 반복횟수
    idx = 0  # a,b를 정하는 인덱스 포인터
    while left:  # 남은 횟수만큼 시행
        left -= 1
        a, b = orders[idx]
        target[a], target[b] = target[b], target[a]
        idx += 1
        idx %= len(orders)

    ans = ''  # ?
    for i in target:
        ans += str(i)
    print(f'#{test_case}', ans)
