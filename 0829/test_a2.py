T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    houses = []
    house_coords = set()
    for _ in range(N):
        h_info = list(map(int, input().split()))
        houses.append(h_info)
        house_coords.add((h_info[0], h_info[1]))

    min_dist = 20*30
    flag = True
    for charges in range(1, 3):
        if charges == 1:
            for x in range(-15, 16):
                for y in range(-15, 16):
                    dist = 0
                    if (x, y) not in house_coords:
                        for house in houses:
                            if abs(house[0]-x) + abs(house[1]-y) > house[2]:
                                break
                            dist += abs(house[0]-x) + abs(house[1]-y)
                        else:
                            if min_dist > dist:
                                min_dist = dist
                            flag = False
        else:
            if flag:
                for x_1 in range(-15, 16):
                    for y_1 in range(-15, 16):
                        for x_2 in range(-15, 16):
                            for y_2 in range(-15, 16):
                                total_dist = 0
                                if (x_1, y_1) not in house_coords and (x_2, y_2) not in house_coords and\
                                        (x_1, y_1) != (x_2, y_2):
                                    for house in houses:
                                        dist_1 = abs(house[0] - x_1) + abs(house[1] - y_1)
                                        dist_2 = abs(house[0] - x_2) + abs(house[1] - y_2)
                                        dist = min(dist_1, dist_2)
                                        if dist > house[2]:
                                            break
                                        total_dist += dist
                                    else:
                                        if min_dist > total_dist:
                                            min_dist = total_dist

    if min_dist == 600:
        ans = -1
    else:
        ans = min_dist
    print(f'#{test_case} {ans}')
