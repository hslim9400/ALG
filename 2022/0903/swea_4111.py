
T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    K = int(input())
    cameras = list(map(int, input().split()))

    cameras.sort()
    if K >= N:
        ans = 0
    else:
        dists = []
        for i in range(N-1):
            dist = cameras[i+1] - cameras[i]
            dists.append(dist)  # 카메라가 없는 구간들을 모아준다
        dists.sort(reverse=True)
        # 거꾸로 정렬하면 dist[0]이 카메라가 없는 가장 긴 구간의 길이.
        # 가장 우선적으로 제거
        ans = sum(dists) - sum(dists[:K-1])  # 2개의 수신기면 한개의 구간을 제거할 수 있음
    print(f'#{test_case} {ans}')

