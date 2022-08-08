
T = int(input())

for test_case in range(1, T+1):

    N, M = list(map(int, input().split()))
    height_list = list(map(int, input().split()))
    max_fall = 0

    for i in range(N-1):  # 모든 최고점을 확인하지만 가장 오른쪽 상자는 확인하지 않아도 됨
        fall_height = 0
        for j in range(i+1, N):  # 해당 최고점 오른쪽을 확인
            if height_list[i] > height_list[j]:  # 확인중인 최고점이 오른쪽의 다른 어떤 최고점보다 높으면
                fall_height = fall_height + 1  # 낙하거리 +1
        if fall_height > max_fall:  # 최대 낙하거리와 비교하여 더 큰 값 반환
            max_fall = fall_height

    print(f'#{test_case} {max_fall}')


