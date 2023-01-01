for test_case in range(1, 11):
    # ///////////////////////////////////////////////////////////////////////////////////
    ground = int(input())
    buildings = list(map(int, input().split()))
    rooms = 0  # 조망권을 확보한 방
    for i in range(2, len(buildings)):
        if buildings[i] > buildings[i - 1] and buildings[i] > buildings[i - 2] and buildings[i] > buildings[i + 1] and \
                buildings[i] > buildings[i + 2]:  # 좌우로 두칸 씩 확인하여 조망권을 가진 건물인지 확인
            # 주변의 빌딩들과 비교하여 가장 적은 높이 차 만큼 조망권이 있는 방이 있다.
            rooms = rooms + min(buildings[i] - buildings[i - 1], buildings[i] - buildings[i - 2],
                                buildings[i] - buildings[i + 1], buildings[i] - buildings[i + 2])

    print(f'#{test_case} {rooms}')