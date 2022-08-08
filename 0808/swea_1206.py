for test_case in range(1, 11):
    # ///////////////////////////////////////////////////////////////////////////////////
    ground = int(input())
    buildings = list(map(int, input().split()))
    rooms = 0
    for i in range(2, len(buildings)):
        if buildings[i] > buildings[i - 1] and buildings[i] > buildings[i - 2] and buildings[i] > buildings[i + 1] and \
                buildings[i] > buildings[i + 2]:
            rooms = rooms + min(buildings[i] - buildings[i - 1], buildings[i] - buildings[i - 2],
                                buildings[i] - buildings[i + 1], buildings[i] - buildings[i + 2])

    print(f'#{test_case} {rooms}')