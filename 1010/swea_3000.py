import heapq

T = int(input())
for test_case in range(1, T+1):
    N, A = map(int, input().split())
    ans = 0
    mid = A
    left_heap = []  # 중간값 좌측, 최대 힙
    right_heap = []  # 중간값 우측, 최소 힙
    for i in range(N):
        p, q = map(int, input().split())
        mids = []  # 전체 숫자들 중 가운데 세 개의 숫자들을 모을 배열
        mids.append(mid)
        if mid > p:  # 첫 번째 숫자에 대해 시행
            heapq.heappush(left_heap, -p)  # 중간값보다 작다면 왼쪽에 넣고
            left_max = -heapq.heappop(left_heap)  # 왼쪽 애들 중 가장 큰 놈을 골라
            mids.append(left_max)  # 세 개의 숫자에 포함시킨다
        else:  # 크다면 오른 쪽
            heapq.heappush(right_heap, p)
            right_max = heapq.heappop(right_heap)
            mids.append(right_max)

        if mid > q:  # 두 번째 숫자에 대해서도 시행
            heapq.heappush(left_heap, -q)
            left_max = -heapq.heappop(left_heap)
            mids.append(left_max)
        else:
            heapq.heappush(right_heap, q)
            right_max = heapq.heappop(right_heap)
            mids.append(right_max)
        mids.sort()  # 세 숫자를 모은 배열을 정렬
        mid = mids[1]  # 가운데가 중간 값
        heapq.heappush(left_heap, -mids[0])  # 작은 놈은 왼쪽에
        heapq.heappush(right_heap, mids[2])  # 큰 놈은 오른쪽에
        ans += mid  # 답을 더해줌
    ans %= 20171109

    print(f'#{test_case} {ans}')
