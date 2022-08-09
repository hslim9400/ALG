
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    K, N, M = list(map(int, input().split()))
    stops = list(map(int, input().split()))
    dists = [stops[0]]  # 0부터 첫 정류장까지의 거리
    ans = 1  # 필요시 0으로 답을 출력하기 위한 설정
    for i in range(1, M):
        dists = dists + [stops[i] - stops[i-1]]  # 정류장간의 거리들을 리스트에 저장
    dists = dists + [N - stops[-1]]  # 마지막 정류장과 종점간의 거리

    for i in range(M-1):
        if dists[i] > K:  # 최대 배터리로 갈 수 없는 곳이 있을 경우
            ans = 0
            break

    if ans == 0:
        print(f'#{test_case} {ans}')  # 0을 출력하고 해당 testcase 종료
        continue

    bat = K
    for i in range(M):
        bat = bat - (dists[i])  # 다음 정류장으로 이동시 배터리 소모
        if bat < (dists[i+1]):  # 배터리가 모자랄 시
            bat = K  # 배터리를 충전하고
            ans = ans + 1  # 배터리 충전회수 + 1

    print(f'#{test_case} {ans-1}')
    # ///////////////////////////////////////////////////////////////////////////////////